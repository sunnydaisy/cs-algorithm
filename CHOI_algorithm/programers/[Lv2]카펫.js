function solution(brown, yellow) {
    var answer = [3, 3];
    let yelloGrid = [1, 1];
    let browMoveCount = (brown - 8) / 2;
    let move = [ parseInt(browMoveCount / 2), parseInt(browMoveCount / 2)];

    if (browMoveCount % 2 == 1) {
        move[0]++;
    }
    while (true) {
        let tmpYelloGrid = [0, 0];
        tmpYelloGrid.map((v, i) => tmpYelloGrid[i] = yelloGrid[i] + move[i]);
        if (tmpYelloGrid[0] * tmpYelloGrid[1] === yellow) break;
        move[0]++;
        move[1]--;
    }
    answer.map((v, i) => answer[i] = answer[i] + move[i]);
    return answer;
}