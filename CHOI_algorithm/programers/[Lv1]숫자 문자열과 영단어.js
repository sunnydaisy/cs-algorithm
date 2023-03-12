function solution(s) {
    let numStrs = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    
    numStrs.forEach((numStr, idx) => {
        s = s.replaceAll(numStr, "" + idx);
    })
    
    return +s;
}