/**
 * 1차 시도 실패 74.1 / 100.0
 * 2차 시도 실패 74.1 / 100.0
 */
function leftTargetLength(name, idx) {
    let result = 0;
    let moveIdx = idx;
    let flag = true;
    while (moveIdx !== idx || flag) {
        if (name[moveIdx] !== "A") return [result, moveIdx];
        result++;
        moveIdx--;
        if (moveIdx === -1) {
            moveIdx = name.length - 1;
        }
        flag = false;
    };
    return [-1, -1];
};

function rightTargetLength(name, idx) {
    let result = 0;
    let moveIdx = idx;
    let flag = true;
    while (moveIdx !== idx || flag) {
        if (name[moveIdx] !== "A") return [result, moveIdx];
        result++;
        moveIdx++;
        if (moveIdx === name.length) {
            moveIdx = 0;
        }
        flag = false;
    };
    return [0, 0];
};

function getCharChangeCount(targetChar) {
    if ("ZYXWVUTSRQPO".includes(targetChar)) {
        return "ZYXWVUTSRQPO".indexOf(targetChar) + 1;
    }
    if ("ABCDEFGHIJKLMN".includes(targetChar)) {
        return "ABCDEFGHIJKLMN".indexOf(targetChar);
    }
}

function solution(name) {
    var answer = 0;
    let nowIdx = 0;
    let count = 0;
    while (true) {
        let [left, leftMoveIdx] = leftTargetLength(name, nowIdx);
        let [right, rightMoveIdx] = rightTargetLength(name, nowIdx);
        // console.log(`left ${left} leftMoveIdx ${leftMoveIdx}`);
        // console.log(`right ${right} rightMoveIdx ${rightMoveIdx}`);

        if (left === -1 || right === -1) break;
        if (left < right) {
            answer += left + getCharChangeCount(name[leftMoveIdx]);
            nowIdx = leftMoveIdx;
        } else {
            answer += right + getCharChangeCount(name[rightMoveIdx]);
            nowIdx = rightMoveIdx;
        }
        name = name.slice(0, nowIdx) + "A" + name.slice(nowIdx + 1)
        // console.log(`${nowIdx} ${name} answer ${answer}`);
        // count++;
        // if (count === 4) break;
    }
    return answer;
}