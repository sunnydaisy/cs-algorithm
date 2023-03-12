function solution(survey, choices) {
    var answer = '';
    let types = [0, 0, 0, 0];
    let plusType = "TFMN";
    let minusType = "RCJA";
    
    for (let i=0; i<survey.length; i++) {
        
        let choiceDif = choices[i] - 4;
        if (choiceDif < 0) {
            if (plusType.includes(survey[i][0])) {
                types[plusType.indexOf(survey[i][0])] += Math.abs(choiceDif);
            } else {
                types[minusType.indexOf(survey[i][0])] -= Math.abs(choiceDif);
            }
        } else if (choiceDif > 0) {
            if (plusType.includes(survey[i][1])) {
                types[plusType.indexOf(survey[i][1])] += Math.abs(choiceDif);
            } else {
                types[minusType.indexOf(survey[i][1])] -= Math.abs(choiceDif);
            }
        }
        // console.log(types)
    }
    for (let i=0; i<4; i++) {
        if (types[i] <= 0) {
            answer += minusType[i];
        } else {
            answer += plusType[i];
        }
    }
    
    return answer;
}