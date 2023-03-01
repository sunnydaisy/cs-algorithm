function solution(s, skip, index) {
    var answer = '';
    let nextAlph = "abcdefghijklmnopqrstuvwxyz";
    
    for (let alph of skip) {
        nextAlph = nextAlph.replace(alph, "");
    }
    
    for (let alph of s){
        answer += nextAlph[(nextAlph.indexOf(alph) + index) % nextAlph.length];
    }
    
    return answer;
}