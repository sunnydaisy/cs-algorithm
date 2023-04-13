const parent = [];
for(let i=0; i<n; i++) parent.push(i);

function findParent(parent, x) {
    if (parent[x] !== x) parent[x] = findParent(parent, parent[x]);
    return parent[x];
}

function unionParent(parent, x, y) {
    x = findParent(parent, x);
    y = findParent(parent, y);
    if (x < y) parent[y] = x;
    else parent[x] = y;
}

let answer = 0;
for(const cost of costs){
    // 만약 두 섬의 부모가 다르면, 즉 사이클이 형성되지 않은 상태라면
    if(!findParent(parent,cost[0],cost[1])){
        answer += cost[2];	// 정답에 해당 가중치를 더해준다 (오름차순으로 정렬해서 작은값 선택 가능)
        unionParent(parent,cost[0],cost[1]);  // 이제 두 섬은 연결되었으니 합쳐준다
    }
}