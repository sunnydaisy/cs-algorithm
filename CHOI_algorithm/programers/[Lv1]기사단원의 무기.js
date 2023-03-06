function getDivisors(num) {
    let divisors = [];
    let squrt = Math.sqrt(num);
    for (let i=1; i<=squrt; i++){
        if (num % i  == 0){
            divisors.push(i);
            if (i != num / i){
                divisors.push(num / i);
            }
        }
    }
    return divisors;
}


function solution(number, limit, power) {
    var answer = 0;
    
    for (let i=1; i<=number; i++){
        let count = getDivisors(i).length;
        if (count > limit){
            answer += power;
        } else {
            answer += count;
        }
    }
    
    return answer;
}