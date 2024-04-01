/*

Given an array of numbers, add all of the values together but only if the number doesn't repeat a digit.

Example:

> uniqueSum([1,2,3])
> 6

> uniqueSum([11,22,33])
> 0

> uniqueSum([101,2,3]) 
> 5

*/

function uniqueSum(arr) {
   let res =0
   for (let i=0; i < arr.length ; i++) {
      const num = arr[i]
      const numArr = Array.from(String(num), Number);
      const numSet = new Set(numArr)
      if (numSet.size == numArr.length) {
         res += numArr.reduce((a, b) =>a+b, 0)
       }
   }
      
   return res
} 
