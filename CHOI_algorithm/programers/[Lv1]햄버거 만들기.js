function solution(ingredient) {
    var answer = 0;
    
    for (let i = 0; i < ingredient.length - 3; i++){
        if (ingredient.slice(i, i + 4).join("") === "1231"){
            ingredient.splice(i, 4);
            answer++;
            i -= 3;
        }
    }
    return answer;
}