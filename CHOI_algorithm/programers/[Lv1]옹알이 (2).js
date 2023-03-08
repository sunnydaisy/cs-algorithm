/**
 * 실패 90/100
 */

 function strcmp(a, b) {
    for (let i = 0; i < Math.min(a.length, b.length); i++){
        if (a[i] != b[i]) return false;
    }
    return true;
}

function canSplit(bab) {
    let can = [ "aya", "ye", "woo", "ma" ];
    
    for (let word of can) {
        if (strcmp(word, bab)) return word;
    }
    return "";
}

function canSpeack(bab) {
    let i = 0;
    let pastWord = "";
    
    while (i < bab.length){
        let splited = canSplit(bab.slice(i));
        if (splited !== "") {
            if (pastWord !== "" && pastWord === splited) return false;
            i += splited.length;
            pastWord = splited;
            continue;
        }
        return false;
    }
    return true;
}


function solution(babbling) {
    var answer = 0;
    
    
    for (let bab of babbling) {
        if (canSpeack(bab)) answer++;
    }
    
    return answer;
}