function sub(str) {
    let target = str[0];
    let same = 0, div = 0;
    
    for (let i = 0; i<str.length; i++) {
        if (str[i] === target) same++;
        else div++;
        
        if (same === div) {
            return i;
        }
    }
    return -1;
}

function solution(s) {
    var answer = 0;
    
    do {
        let idx = sub(s);
        if (idx === -1) {
            answer++;
            break;
        }
        // console.log(s.slice(0, idx + 1));
        s = s.slice(idx + 1);
        // console.log(s);
        answer++;
    } while (s)
    
    
    return answer;
}