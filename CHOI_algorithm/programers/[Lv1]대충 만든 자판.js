let minTimes = [];

function solution(keymap, targets) {
    var answer = [];
    
    for (let i = 0; i < 26; i++) {
        minTimes.push(101);
    }
    
    for (let keym of keymap) {
        for (let i =0; i<keym.length; i++) {
            let a = keym.charCodeAt(i);
            minTimes[a - 65] = Math.min(minTimes[a - 65], i + 1);
        }
    }
    
    for (let target of targets) {
        let count = 0;
        for (let i =0; i<target.length; i++) {
            let asci = target.charCodeAt(i);
            let minCount = minTimes[asci - 65];
            if (minCount === 101) {
                count = -1;
                break;
            }
            count += minCount;
        }
        answer.push(count);
    }
    
    return answer;
}