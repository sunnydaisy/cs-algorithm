function solution(new_id) {
    var answer = '';
    // to lowerCase
    answer = new_id.split("").map(ch => {
        if ("A" <= ch && ch <= "Z") {
            return ch.toLowerCase();
        } else {
            if (!"abcdefghijklmnopqrstuvwxyz0123456789-_.".includes(ch)){
                return "";
            }
            return ch;
        }
    }).join("");
    answer = answer.split(".").filter(ch => ch).join(".");
    if (!answer){
        answer = "a";
    }

    if (answer.length >= 16) {
        answer = answer.split("").splice(0, 15).join("");
        answer = answer.split(".").filter(ch => ch).join(".");
    }
    while (answer.length < 3) {
        answer += answer[answer.length - 1];
    }

    return answer;
}