/**
 * 실패 90.0 / 100.0
 */
let termMap = new Map();

function initTerm(terms){
    for (let term of terms) {
        let [t, m] = term.split(" ");
        termMap.set(t, +m);
    }
}

function isFinish(now, targetDay) {
    let [nyy, nmm, ndd] = now.split(".").map(a => +a);
    let [tyy, tmm, tdd] = targetDay.split(".").map(a => +a);
    // console.log(`now : ${now}`);
    // console.log(`targetDay : ${targetDay}`);
    
    if (nyy < tyy) return false;
    else if (nyy > tyy) return true;
    else {
        if (nmm < tmm) return false;
        else if (nmm > tmm) return true;
        else {
            if (ndd <= tdd) return false;
            else return true
        }
    }
    
    // if (nyy < tyy) return false;
    // if (nyy === tyy && nmm < tmm) return false;
    // if (nyy === tyy && nmm === tmm && ndd < tdd) return false;
    // // console.log(nyy < tyy);
    // console.log(nmm < tmm);
    // console.log(ndd < tdd);
    return true;
}

function afterMonthEndDay(target, month) {
    let [yy, mm, dd] = target.split(".");
    
    // console.log(`dd : ${dd}`);
    yy = +yy;
    mm = +mm;
    dd = +dd;
    
    while (month > 12) {
        yy++;
        month -= 12;
    }
    
    if (mm + month > 12) {
        yy = yy + 1;
        mm = (mm + month) % 12 ;    
    } else {
        mm += month;
    }
    
    if (dd === 1) {
        if (mm === 1) {
            yy--;
            mm = 12;
        } else {
            mm--;
        }
        dd = 28;
    } else {
        dd--;
    }
    
    
    mm = "" + mm;
    dd = "" + dd;
    mm = mm.padStart(2, '0');
    dd = dd.padStart(2, '0');
    
    return yy+"."+mm+"."+dd;
}

function isTarget(today, terms, privacie) {
    let [date, type] = privacie.split(" ");
    let [yy, mm, dd] = date.split(".");
    let typeMonth = termMap.get(type);
    let endDate = afterMonthEndDay(date, typeMonth);
    // console.log(date + " " + typeMonth + " " + a);
    return isFinish(today, endDate);
}

function solution(today, terms, privacies) {
    var answer = [];
    
    initTerm(terms);
    for (let i = 0; i<privacies.length; i++) {
        if (isTarget(today, terms, privacies[i])) {
            answer.push(i + 1);
        }
        // console.log(afterMonthEndDay(privacies[i].split(" ")[0], 1));
        // console.log(afterMonthEndDay(privacies[i].split(" ")[0], 2));
        // console.log(afterMonthEndDay(privacies[i].split(" ")[0], 3));
        // console.log(afterMonthEndDay(privacies[i].split(" ")[0], 4));
        // console.log(afterMonthEndDay(privacies[i].split(" ")[0], 5));
        // console.log(afterMonthEndDay(privacies[i].split(" ")[0], 10));
        // console.log(afterMonthEndDay(privacies[i].split(" ")[0], 20));
        // console.log(afterMonthEndDay(privacies[i].split(" ")[0], 30));
        // console.log(afterMonthEndDay(privacies[i].split(" ")[0], 50));
        // console.log(afterMonthEndDay(privacies[i].split(" ")[0], 60));
        // console.log(afterMonthEndDay(privacies[i].split(" ")[0], 100));
    }
    
    return answer;
}