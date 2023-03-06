function solution(k, score) {
    var answer = [];
    let honer = [];
    for (let sc of score) {
        if (answer.length < k) {
            honer.push(sc);
        }
        else {
            let min = Math.min(...honer); // 최소값 찾기
            let index = honer.indexOf(min); // 최소값의 인덱스 찾기
            if (min < sc) {
                honer.push(sc);
                honer.splice(index, 1); // 최소값 삭제하기
            }
                
        }
        answer.push(Math.min(...honer));
    }
    return answer;
}