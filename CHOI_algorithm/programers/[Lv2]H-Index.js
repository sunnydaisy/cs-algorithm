function solution(citations) {
    citations = citations.sort((a, b) => b - a);
    for (let h = citations[0]; h > 0; h--) {
        if (citations.filter(c => c >= h).length >= h) return h;
    }
    return 0;
}