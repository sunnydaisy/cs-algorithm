function getCombination(arr, selectNumber) {
    const results = [];

    if (selectNumber === 1) return arr.map(el => [el]);

    arr.forEach((fixed, idx, origin) => {
        const rest = origin.slice(idx + 1);
        const combinations = getCombination(rest, selectNumber - 1);
        const attached = combinations.map(el => [fixed, ...el]);
        results.push(...attached);
    });
    return results;
}

let combination = getCombination([1,2,2], 2);
console.log(combination);
