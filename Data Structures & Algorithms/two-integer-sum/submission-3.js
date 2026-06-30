class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hashmap = {};
        for (let i = 0; i < nums.length; i++) {
            let diff = target - nums[i];
            if (hashmap[nums[i]] !== undefined) {
                return [Math.min(i, hashmap[nums[i]]), Math.max(i, hashmap[nums[i]])];
            } else {
                hashmap[diff] = i;
            }
        }
    }
}

