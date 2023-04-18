/**
 * 정확성: 30.8
 * 합계: 30.8 / 100.0
 */
function findParent(parents, n) {
    if (n !== parents[n]) parents[n] = findParent(parents, parents[n]);
    return parents[n];
}

function unionParents(parents, a, b) {
    a = findParents(parents, a);
    b = findParents(parents, b);
    if (a < b) {
        parents[b] = a;
    } else {
        parents[a] = b;
    }
}

function solution(n, computers) {
    var answer = 0;
    let parents = new Array(n + 1).fill(0).map((v, i) => i);

    computers.forEach(line => {
        let parent;
        line.forEach((v, i) => {
            if (v === 1) {
                if (!parent) {
                    parent = i + 1;
                } else {
                    parents[i + 1] = parent;
                }
            }
        })
    });

    parents = parents.map(v => findParent(parents, v));
    console.log(new Set(parents.slice(1)))
    return new Set(parents.slice(1)).size;
}