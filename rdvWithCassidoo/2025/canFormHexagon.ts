/*
Given an array of side lengths, write a function to determine they can form a 
hexagon with three side-length pairs (as in, three pairs of equal sides 
needed). Return true if possible.
*/ 

function canFormHexagon (myList:Number[]): boolean { 
    if (myList.length != 6) {
        return false
    }

    // each side must be present 2, 4 of 6 times. Else: return false

    // Notes: 
    // - doing an old fashion "for" because it runs faster than "foreach"
    // - don't need to check the last item
    for (let i=0; i<myList.length - 1; i++) { 

        const currentSide = myList[i]
        // There is probably faster code, but this was fast to implement, it works, and I can understand it
        const nbOfOccurenceOfThisSide = myList.filter((x) => x == currentSide).length
        if (![2,4,6].includes(nbOfOccurenceOfThisSide)){
            return false
        }
    }
    return true
}

console.log("VERY BASIC UNIT TEST")
console.log("these must be false")

console.log(canFormHexagon([1, 2, 3, 4, 5, 6]))
console.log(canFormHexagon([1,2]))
console.log(canFormHexagon([2, 2, 2, 2, 2, 2, 2]))
console.log(canFormHexagon([2, 3, 8, 8, 2, 3, 3]))
console.log(canFormHexagon([2, 2, 8, 8, 2, 3]))
console.log(canFormHexagon([2, 2, 2, 2, 3, 1]))


console.log("these must be true")
console.log(canFormHexagon([2, 2, 2, 2, 2, 2]))
console.log(canFormHexagon([2, 2, 2, 2, 3, 3]))
console.log(canFormHexagon([2, 3, 8, 8, 2, 3]))
