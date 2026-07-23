class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let len = nums.length
        let memo = new Array(len).fill(0)
        let max = nums[0]

        if (len === 1) return nums[0]
        memo[0] = nums[0]
        for (let i = 1; i < len; i++) {
            memo[i] = Math.max(memo[i-1] + nums[i], nums[i])
            max = Math.max(max, memo[i])
        }
        return max
    }
}
