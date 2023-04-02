function solution(N, stages) {
    var answer = [];
    let diffcalty = [];

    for (let i = 1; i < N + 1; i++) {
        let info = {
            stage : i,
            diffcalty : 0
        }
        const retchCount =  stages.filter(s => s >= i).length;
        const failCount = stages.filter(s => s === i).length;
        if (retchCount === 0)
            info.diffcalty = 0;
        else {
            info.diffcalty = (failCount / retchCount);
        }
        diffcalty.push(info);
    }
    diffcalty.sort((a, b) =>  b.diffcalty - a.diffcalty)
    diffcalty.forEach(info => answer.push(info.stage))

    return answer;
}