function solution(nums) {
    let ableCount = nums.length / 2;
    const c = new Set(nums).size;
    return Math.min(ableCount, c);
}