function pickDoll(board, col) {
    let ret = 0;
    for (let i = 0; i <board.length; i++) {
        if (board[i][col] != 0) {
            ret = board[i][col];
            board[i][col] = 0;
            return ret;
        }
    }
    return ret;
}

function dismissDoll(arr) {
    if (arr.length >= 2) {
        if (arr[arr.length - 1] === arr[arr.length - 2]) {
            arr.splice(arr.length - 2, arr.length);
            return 2;
        }
    }
    return 0;
}

function solution(board, moves) {
    var answer = 0;
    const basket = [];

    moves.forEach((move) => {
        const col = move - 1;
        const pickResult = pickDoll(board, col);
        if (pickResult != 0) {
            basket.push(pickResult);
            answer += dismissDoll(basket);
        }
    })

    return answer;
}