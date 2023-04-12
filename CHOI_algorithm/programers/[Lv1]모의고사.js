function solution(answers) {
    let giveUp = {
        "1" : [ 1, 2, 3, 4, 5],
        "2" : [2, 1, 2, 3, 2, 4, 2, 5],
        "3" : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    let answerCount = [0, 0, 0];
    answers.forEach((an, i) => {
        giveUp["1"][i % 5] === an ? answerCount[0]++ : null;
        giveUp["2"][i % 8] === an ? answerCount[1]++ : null;
        giveUp["3"][i % 10] === an ? answerCount[2]++ : null;
    })
    let maxCount = Math.max(...answerCount);
    answerCount = answerCount.map((count, i) => [count, i])
        .sort((a, b) => a[0] - b[0] || a[1] - b[1])
        .filter(([count, i]) => count === maxCount)
        .map(([count, i]) => i + 1)
    return answerCount;
}