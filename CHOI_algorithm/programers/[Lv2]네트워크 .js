/**
 * DFS 풀이
 */
function dfs(node, visited, computers) {
    visited[node] = true;

    for (let i = 0; i < computers.length ; i++) {
        if (computers[node][i] && !visited[i]) {
            dfs(i, visited, computers);
        }

    }
}

function solution(n, computers) {
    var answer = 0;
    let visited = [];

    for (let i = 0; i < n ; i ++) {
        if (!visited[i]) {
            answer++;
            dfs(i, visited, computers);
        }
    }

    return answer;
}