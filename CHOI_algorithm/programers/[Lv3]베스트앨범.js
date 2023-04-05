function solution(genres, plays) {
    var answer = [];
    let infos = new Map();
    let totalPlayCount = new Map();

    for (let i = 0; i < genres.length; i++) {
        if (!infos.has(genres[i])) {
            infos.set(genres[i], []);
            totalPlayCount.set(genres[i], 0);
        }
        infos.get(genres[i]).push([i, plays[i]]);
        totalPlayCount.set(genres[i], totalPlayCount.get(genres[i]) + plays[i]);
    }

    Array.from(totalPlayCount).sort((a, b) => b[1] - a[1])
        .forEach(([gen]) => {
            infos.get(gen).sort((a, b) => b[1] - a[1] || a[0] - b[0]);
            infos.get(gen).splice(0, 2)
                .forEach(([idx]) => {
                    answer.push(idx);
                })
        })

    return answer.slice();
}