// 속도 만큼 진전되는 함수
function progess(progresses, speeds) {
    progresses.forEach((val, idx) => {
        progresses[idx] += speeds[idx];
    });
}

function solution(progresses, speeds) {
    var answer = [];
    let fullfiled = 0;

    progresses.reverse()
    speeds.reverse()

    while (progresses.length > 0) {
        if (progresses[progresses.length - 1] >= 100) {
            fullfiled++;
            progresses.pop();
            speeds.pop();
            continue;
        }
        if (fullfiled > 0) {
            answer.push(fullfiled);
            fullfiled = 0;
        }
        progess(progresses, speeds);
    }
    if (fullfiled > 0) {
        answer.push(fullfiled);
        fullfiled = 0;
    }



    return answer;
}