function solution(s) {
    let asciArr = Array.from({length : 26}, () => -1);
    var answer = [];
    
    for (let i = 0; i<s.length; i++) {
        let asci = s.charCodeAt(i)
        if (asciArr[asci - 97] === -1) {
            answer.push(-1);
        } else {
            answer.push(i - asciArr[asci - 97])
        }
        asciArr[asci - 97] = i;
    }
    
    return answer;
}