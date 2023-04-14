let arr = [0, 0];
let arr2 = [1, 2];

arr.forEach((v, i) => arr[i] = arr[i] + arr2[i]);
console.log(arr)