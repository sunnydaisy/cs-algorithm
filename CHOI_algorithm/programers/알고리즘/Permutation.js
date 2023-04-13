function getPermutation(arr, selectNumber) {
    const results = [];

    if (selectNumber === 1) return arr.map(el => [el]);

    arr.forEach((fixed, idx, origin) => {
        const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
        const permutation = getPermutation(rest, selectNumber - 1);
        const attached = permutation.map(el => [fixed, ...el]);
        results.push(...attached);
    });
    return results;
}


let permutation = getPermutation([1,2,3], 2);
console.log(permutation);
