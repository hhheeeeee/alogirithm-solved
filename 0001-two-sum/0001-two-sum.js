/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 
var twoSum = function(nums, target) {
   let answer
   nums.map((num, index) => {
     nums.map((num2, index2) => {
      if (index2 > index && num + num2 === target) {
        answer = [index, index2];
      }
     })
   })
   return answer
    
};