
function solution(k, m, score) {
    var answer = 0;
    
    score.sort(function(a, b) {
        return b - a;
    });
    
    for (let i = m - 1 ; i < score.length; i+=m) {
        // console.log(`i : ${i}`);
        answer += score[i] * m;
    }
    return answer;
}

 