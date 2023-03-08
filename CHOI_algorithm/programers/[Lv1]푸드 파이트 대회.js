function solution(food) {
    let order = "";
    
    for (let i = 1; i<food.length; i++){
        let calOrd = i + "";
        order += calOrd.repeat(parseInt(food[i] / 2));
    }
    return order + "0" + [...order].reverse().join("");
}