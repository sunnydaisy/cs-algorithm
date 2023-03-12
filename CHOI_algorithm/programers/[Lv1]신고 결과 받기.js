// https://school.programmers.co.kr/learn/courses/30/lessons/92334

function solution(id_list, report, k) {
    var answer = Array.from({length : id_list.length}, () => 0);
    let userInfos = {};

    for (let id of id_list) {
        userInfos[id] = {
            reportedCount : 0,
            reportedList : [],
        }
    }
    
    report.map((str) => str.split(" "))
        .forEach(([reporter, target]) => {
            if (!userInfos[target].reportedList.includes(reporter)){
                userInfos[target].reportedCount++;
                userInfos[target].reportedList.push(reporter);    
            }
    })
    
    for (let id in userInfos) {
        if (userInfos[id].reportedCount >= k) {
            userInfos[id].reportedList.forEach((name) => {
                answer[id_list.indexOf(name)]++;
            })
        }
    }
    
    
    return answer;
}