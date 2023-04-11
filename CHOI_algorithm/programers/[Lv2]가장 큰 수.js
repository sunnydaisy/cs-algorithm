


/*
first trial failed
 */
function getNextNum(str, i) {
    if (!str[i + 1]) return [true, +str[str.length - 1]];
    return [false, +str[i + 1]];
}

function solution(numbers) {

    return numbers.map(num => "" + num)
        .sort((a, b) => {
            let i = -1;
            let aNext, bNext;
            let aFinish;
            let bFinish;
            // console.log(`a ${a} `)
            // console.log(`b ${b} `)
            do {
                i++;
                [aFinish, aNext] = getNextNum(a, i);
                [bFinish, bNext] = getNextNum(b, i);
                // console.log(`aNext ${aNext} `)
                // console.log(`bNext ${bNext} `)
            } while (!(aFinish && bFinish) && aNext === bNext)
            return bNext - aNext;

//             return b[i] - a[i];
        }).join("");
}