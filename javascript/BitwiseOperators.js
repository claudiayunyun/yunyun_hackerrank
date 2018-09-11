let result = 0;
let size = Math.ceil(Math.log(n));
console.log(size)
for(let a = 1; a <= n; a++) {
    for(let b = a + 1; b <= n; b++) {
        let bitA = [];
        let bitB = [];
        for(let i = 0; i < size; i++ ) {
            bitA.push(a % 2);
            a = a / 2;
            bitB.push(b % 2);
            b = b / 2;
        }
        let bitAnd = [];
        let tenBase = 0;
        for(let i = 0; i < bitA.length; i++) {
            bitAnd.push(bitA[i] || bitB[i]);
        }
        for(let bit of bitAnd) {
            tenBase = tenBase * 2 + bit; 
        }
        if (tenBase > result && tenBase < k) {
            result = tenBase;
        }
    }
}
return result;