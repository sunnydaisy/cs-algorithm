const graph = {
    A: ["B", "C"],
    B: ["A", "D"],
    C: ["A", "G", "H", "I"],
    D: ["B", "E", "F"],
    E: ["D"],
    F: ["D"],
    G: ["C"],
    H: ["C"],
    I: ["C", "J"],
    J: ["I"]
};

function DFS(graph, startNode) {
    let visited = [];
    let needVisited = [startNode];

    while (needVisited.length !== 0) {
        const node = needVisited.shift();
        if (!visited.includes(node)) {
            visited.push(node);
            needVisited = [...graph[node] , ...needVisited];
        }
    };
    return visited;
}

let result = DFS(graph, "A");
console.log(result);