/**
 * 2차 시도 성공
 * 정렬 추가하니까 통과함
 */

function solution(n, lost, reserve) {
    var answer = n;
    let have = new Array(n + 1).fill(1); // 0도 포함하고 나중에 0인 사람만 n 에서 뺸다
    lost = lost.sort((a, b) => a - b);
    reserve = reserve.sort((a, b) => a - b);
    lost.forEach(num => {
        let extraIdx = reserve.indexOf(num);
        if (extraIdx === -1) have[num] = 0;
        else {
            reserve[extraIdx] = 0;
        }
    });

    reserve.forEach(num => {
        if (num === 0) {
            return ;
        }
        if (!have[num - 1]) {
            have[num - 1] = 1;
        } else if (!have[num + 1]) {
            have[num + 1] = 1;
        }
    })
    return n - have.filter(v => v===0).length;
}