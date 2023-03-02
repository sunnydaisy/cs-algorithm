function solution(t, p) {
    var answer = 0;
    let len = p.length;
    
    for (let i = 0; i<=t.length - len; i++) {
        let compNum = t.substr(i, len);
        if (+compNum <= +p) answer++;
    }
    
    return answer;
}