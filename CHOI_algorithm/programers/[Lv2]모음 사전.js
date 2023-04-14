const words = ["", "A", "E", "I", "O", "U"];

function isDone(info) {
    return info["0"] === 5 &&
        info["1"] === 5 &&
        info["2"] === 5 &&
        info["3"] === 5 &&
        info["4"] === 5
}

function getWord(info) {
    let result = words[info["0"]] +  words[info["1"]] +  words[info["2"]] +
        words[info["3"]] +  words[info["4"]];
    return result;
}

function addInfo(info) {
    if (info["0"] === 0) {
        info["0"]++;
        return ;
    }
    if (info["1"] === 0) {
        info["1"]++;
        return ;
    }
    if (info["2"] === 0) {
        info["2"]++;
        return ;
    }
    if (info["3"] === 0) {
        info["3"]++;
        return ;
    }
    if (info["4"] === 0) {
        info["4"]++;
        return ;
    }

    info["4"]++;
    if (info["4"] === 6) {
        info["4"] = 0;
        info["3"]++;
    }
    if (info["3"] === 6) {
        info["3"] = 0;
        info["2"]++;
    }
    if (info["2"] === 6) {
        info["2"] = 0;
        info["1"]++;
    }
    if (info["1"] === 6) {
        info["1"] = 0;
        info["0"]++;
    }
}


function solution(word) {
    var answer = 0;
    let info = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0
    };
    while (!isDone(info)) {
        if (getWord(info) === word) break;
        addInfo(info);
        answer++;
    }
    return answer;
}