/**
 * find-union 풀이
 */

function findParent(parents, n) {
    if (n !== parents[n]) parents[n] = findParent(parents, parents[n]);
    return parents[n];
}

function unionParents(parents, a, b) {
    a = findParent(parents, a);
    b = findParent(parents, b);
    if (a < b) {
        parents[b] = a;
    } else {
        parents[a] = b;
    }
}

function solution(n, computers) {
    var answer = 0;
    let parents = new Array(n + 1).fill(0).map((v, i) => i);

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i !== j && computers[i][j]) {
                unionParents(parents, i + 1, j + 1);
            }
        }
    }
    parents = parents.map(v => findParent(parents, v))
    return [...new Set(parents)].length - 1;
}