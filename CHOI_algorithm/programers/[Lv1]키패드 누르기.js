const keypad = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]];

function moveLength(num, pos) {
    for (let i = 0; i < 4; i ++) {
        for (let j = 0; j < 4; j ++) {
            if (keypad[i][j] === num) {
                return {
                    lcount : Math.abs(pos["left"][0] - i) + Math.abs(pos["left"][1] - j),
                    rcount : Math.abs(pos["right"][0] - i) + Math.abs(pos["right"][1] - j),
                    pos : [i, j]
                };
            }
        }
    }
}

function solution(numbers, hand) {
    var answer = '';

    const pos = {
        left : [3, 0],
        right : [3, 2]
    };

    numbers.forEach(num => {
        let info = moveLength(num, pos);
        if ([1,4,7].includes(num)) {
            answer += "L";
            pos["left"] = info.pos;
        } else if ([3,6,9].includes(num)){
            answer += "R";
            pos["right"] = info.pos;
        }
        else {
            if (hand === "left") {
                if (info.lcount <= info.rcount) {
                    answer += "L";
                    pos["left"] = info.pos;
                } else if (info.lcount > info.rcount) {
                    answer += "R";
                    pos["right"] = info.pos;
                }
            } else {
                if (info.lcount < info.rcount) {
                    answer += "L";
                    pos["left"] = info.pos;
                } else if (info.lcount >= info.rcount) {
                    answer += "R";
                    pos["right"] = info.pos;
                }
            }
        }
    })

    return answer;
}