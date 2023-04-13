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

function BFS(graph, startNode) {
    let visited = [];
    let needVisited = [startNode];

    while (needVisited.length !== 0) {
        const node = needVisited.shift();
        if (!visited.includes(node)) {
            visited.push(node);
            needVisited = [...needVisited, ...graph[node]];
        }
    };
    return visited;
}

let result = BFS(graph, "A");
console.log(result);