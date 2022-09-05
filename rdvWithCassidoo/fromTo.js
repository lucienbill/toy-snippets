function fromTo(start, end){
    let n = start - 1
    return function(){
        if (n < end){
            n += 1
            return n
        }
        return undefined
    }
}

// UNIT TEST
let isFail = false 
test = (actual, expected) => {
    try {
        if (actual === expected){
            console.info(`✅ Test OK (actual === expected === ${actual})`)
        } else {
            console.error(`❌ Test FAILED : (actual, expected) = (${actual}, ${expected})`)
            isFail = true
        }
    } catch (error) {
        isFail = true
    }
}
console.info("--- Unit Test : START ---")

gen = fromTo(5,7)
test(gen(), 5)
test(gen(), 6)
test(gen(), 7)
test(gen(), undefined)
test(gen(), undefined)

if (isFail){
    console.error("\n❌ UNIT TESTS : fail")
} else {
    console.info("\n✅ UNIT TESTS : pass")
}
console.info("--- Unit Test : START end---")
