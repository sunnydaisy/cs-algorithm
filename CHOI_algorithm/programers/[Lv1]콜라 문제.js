function solution(a, b, n) {
    var answer = 0;
    while (true) {
        let newCola = parseInt(n / a) * b;
        if (newCola === 0) break;
        n -=  parseInt(n / a) * a;
        n += newCola;
        answer += newCola;
    }
    return answer;
}