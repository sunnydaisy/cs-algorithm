function solution(n, arr1, arr2) {
    let answer = [];
    arr1.forEach(code => {
        code = code.toString(2).padStart(n, "0");
    })

    for (let i = 0; i < n ; i++) {
        let arr1Code = arr1[i].toString(2).padStart(n, "0");
        let arr2Code = arr2[i].toString(2).padStart(n, "0");
        let sumCode = "";
        for (let j = 0; j < n ; j++) {
            arr1Code[j] === '0' && arr2Code[j] === '0' ? sumCode+=" " : sumCode+="#"
        }
        answer.push(sumCode);
    }
    return answer;
}