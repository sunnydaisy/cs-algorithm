function getPrimeArr(n) {
    let result = Array(n + 1).fill(true).fill(false, 0, 2);

    for (let i = 2; i * i <= n; i++) {
        if (result[i]) {
            for (let j = i * i; j <= n; j += i) {
                result[j] = false;
            }
        }
    }
    return result;
}

function getPermutation(arr, selectNumber) {
    let result = [];

    if (selectNumber === 1) return arr.map(el => el);

    arr.forEach((fixed, idx, origin) => {
        const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)]
        const combinations = getPermutation(rest, selectNumber - 1);
        const attached = combinations.map((el) => fixed + el);
        result.push(...attached);
    })
    return result;
}

function solution(numbers) {
    var answer = [];
    let primse = getPrimeArr(9999999);
    numbers = Array.from(numbers);

    for (let i = 1; i <= numbers.length; i++) {
        let re = new Set(getPermutation(numbers, i));
        re = Array.from(re)
            .map(el => +el);
        answer = [...re, ...answer];
    }
    return Array.from(new Set(answer))
        .filter(el => primse[el])
        .length;

}