function getMaxLessThanK(n, k) {
    let max = -1;
    for(let i = 1; i <= n; i++) {
        for(let j = 1; j < i; j++) {
            if((i&j) > max && (i&j) < k) {
                max = i&j;
            }
        }
    }
    return max;
}

console.log(getMaxLessThanK(2, 2));