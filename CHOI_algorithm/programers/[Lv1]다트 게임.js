
function handleBonus(scores, type) {
    if (type === "D") {
        scores[scores.length - 1] =  scores[scores.length - 1] ** 2;
    }
    if (type === "T") {
        scores[scores.length - 1] =  scores[scores.length - 1] ** 3;
    }
}

function handleOption(scores, type) {
    const nowIdx = scores.length - 1;
    const preIdx = nowIdx - 1;
    if (type === "*") {
        scores[nowIdx] = scores[nowIdx] * 2;
        preIdx >= 0 ? scores[preIdx] = scores[preIdx] * 2 : "";
    } else {
        scores[nowIdx] = -scores[nowIdx];
    }
}

function solution(dartResult) {
    let scores = [];
    let tmpNum = "";

    Array.from(dartResult).forEach(ch => {
        if ("SDT".includes(ch)) {
            if (tmpNum){
                scores.push(Number(tmpNum));
                tmpNum = "";
            }
            handleBonus(scores, ch)
        } else if ("*#".includes(ch)) {
            if (tmpNum){
                scores.push(Number(tmpNum));
                tmpNum = "";
            }
            handleOption(scores, ch);
        } else {
            tmpNum += ch;
        }
    })
    return scores.reduce((acc, v) => acc + v);
}