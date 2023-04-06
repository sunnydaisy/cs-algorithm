function solution(s){
    let result = true;
    let leftCount = 0;
    Array.from(s).forEach((val) => {
        if (val === "(") leftCount++;
        else {
            if (leftCount <= 0){
                result = false;
                return ;
            }
            leftCount--;
        }
    })
    if (leftCount > 0) result = false;
    return result;
}