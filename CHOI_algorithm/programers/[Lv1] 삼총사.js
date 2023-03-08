function solution(number) {
    var answer = 0;
    
    const combination = (cur, start) => {
        if (cur.length === 3) {
            answer += cur.reduce((acc, n) => acc + n, 0) === 0 ? 1 : 0;
            return ;
        }
        for (let i = start; i < number.length; i++) {
            combination([...cur, number[i]], i + 1);
        }
    }
    combination([], 0);
    
    return answer;
}