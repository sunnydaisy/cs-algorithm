function solution(clothes) {
    var answer = 1;
    let clothObj = {};
    clothes.forEach((cloth) => {
        if (!clothObj[cloth[1]]) clothObj[cloth[1]] = [];
        clothObj[cloth[1]]  = [...clothObj[cloth[1]], cloth[0]];
    })

    Object.values(clothObj).forEach(vals => {
        answer *= vals.length + 1;
    });
    return answer - 1;
}