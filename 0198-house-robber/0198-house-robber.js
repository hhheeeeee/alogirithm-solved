/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
    if (nums.length === 1) return nums[0]
    let memo = new Array(nums.length).fill(0) // 0 1 2 3 1
    memo[0] = nums[0]
    memo[1] = nums[1]
    for (let i = 2; i < nums.length; i++) {
        if (i == 2) {
            memo[i] = nums[i] + memo[i - 2]
        } else {
            memo[i] = Math.max(nums[i] + memo[i - 2], nums[i] + memo[i - 3])
        }
    }
    return Math.max(memo[nums.length - 1], memo[nums.length - 2])
};