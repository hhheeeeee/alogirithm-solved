/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
    let numset = new Set(nums);
    let length = 0;
    for (let num of numset) {
        if (!numset.has(num - 1)) {
            let current = num;
            let streak = 1;
            while (numset.has(current + 1)) {
                current++;
                streak++;
            }
            length = Math.max(length, streak)
        }
    }

    return length;
};