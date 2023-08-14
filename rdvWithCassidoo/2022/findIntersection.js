/* 
Instructions:

Given two arrays A and B, return the indices at which the two arrays intersect.
If the two arrays have no intersection at all, return null. 
Extra credit: how would you change your code if they were linked lists instead
of arrays, if the input were the two head nodes, and you returned the 
intersection node?

Example:

let listA = [1,4,5,6]
let listB = [2,3,4,5,6]

> findIntersection(listA, listB)
> [1, 2]

(see this diagram[1] if it helps you visualize it)
[1] : https://i.imgur.com/UyglRcN.png

*/

findIntersection = (listA,listB) => {
    let a_i = 0
    for(a of listA){
        if (listB.includes(a)){
            for(b_i =0 ; b_i < listB.length ; b_i ++){
                if(a === listB[b_i]){
                    return [a_i, b_i]
                }
            }
        }
        else { // go to next element of listA
            a_i += 1
        }
    } 
    return null
}
