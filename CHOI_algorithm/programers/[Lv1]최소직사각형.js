function solution(sizes) {
    var answer = 0;
    let [long, short] = [0, 0];
    for (let [w, h] of sizes) {
        let [tmpLong, tmpShort] = w > h ? [w, h] : [h, w];

        long = Math.max(long, tmpLong);
        short = Math.max(short, tmpShort);
    }
    return long * short;
}