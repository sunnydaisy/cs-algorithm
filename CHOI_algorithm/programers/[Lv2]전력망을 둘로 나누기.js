/**
 * 1차 시도 실패 30/100
 */

function findParent(parent, n) {
    if (parent[n] !== n) parent[n] = findParent(parent, parent[n]);
    return parent[n];
}

function unionParent(parent, a, b) {
    a = findParent(parent, a);
    b = findParent(parent, b);
    if (a < b) parent[b] = a;
    else parent[a] = b;
}

function getDiff(arr) {
    let answer = 0;
    let target = arr[0];
    arr.forEach(v => {
        v === target ? answer++ : answer--
    });
    return Math.abs(answer);
}

function solution(n, wires) {
    let parent = new Array(n + 1).fill(0).map((_, i) => i);
    var answer = 1000000000;
    wires.forEach((removeTarget, i) => {
        let tmpWires = [...wires.slice(0, i), ...wires.slice(i + 1)];
        for (let wire of tmpWires) {
            let [x, y] = wire;
            unionParent(parent, x, y);
        }
        answer = Math.min(answer, getDiff(parent.slice(1)));
        parent = new Array(n + 1).fill(0).map((_, i) => i);
    })


    return answer;
}