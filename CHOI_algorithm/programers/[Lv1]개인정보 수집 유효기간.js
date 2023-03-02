let termMap = new Map();

function initMap(terms){
    for (let term of terms) {
        let[type, month] = term.split(" ");
        termMap.set(type, +month);
    }
}

class Date {
    year;
    month;
    day;
    
    constructor(str) {
        let [yy, mm, dd] = str.split(".");
        this.year = +yy;
        this.month = +mm;
        this.day = +dd;
    }
    
    // this 가 더 과거인지 여부
    isPrevOrSame(date) {
        if (date.year > this.year) return true;
        else if (date.year < this.year) return false;
        
        if (date.month > this.month) return true;
        else if (date.month < this.month) return false;
        
        if (date.day >= this.day) return true;
        else if (date.day < this.day) return false;
    }
    
    afterMonth(month) { 
        this.month += month;
        while (this.month > 12) {
            this.month -= 12;
            this.year++;
        }
    }
    
    toString(){
        return `year : ${this.year} month : ${this.month} day : ${this.day}`
    }
}

function solution(today, terms, privacies) {
    var answer = [];
    let todayIm = new Date(today);
    initMap(terms);
    
    for (let i = 0; i<privacies.length; i++){
        let priv = privacies[i];
        let [dateStr, type] = priv.split(" ");
        let tmpIm = new Date(dateStr);
        tmpIm.afterMonth(termMap.get(type));
        if (tmpIm.isPrevOrSame(todayIm)){
            answer.push(i + 1);
        }
    }
    return answer;
}