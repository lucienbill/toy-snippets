/* 
=== Instructions ===

Given an integer n, count the total number of 1 digits appearing in all
non-negative integers less than or equal to n.

--- Example ---
> numberOfOnes(14)
> 7 // 1, 10, 11, 12, 13, 14
*/

const numberOfOnes = (n) => {
    let ones = 0
    for (let x=n; x > 0; x--){
        ones += x.toString().split("").filter(d => d == 1).length
    }
    return ones
}

const numberOfOnesRec = (n) => { // limit : n < 10462
    /*
    This is resursive \o/
    But... it crashes completely on my machine if n > 10461 : 
        'RangeError: Maximum call stack size exceeded'
    So... yeah. Just don't use thise one.
    */
    if (n<1) {
        return 0
    }
    ones = n.toString().split("").filter(x => x == 1).length
    return ones + numberOfOnes(n-1)
}
