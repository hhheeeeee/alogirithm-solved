class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        let result = [];

        let recursive = (curIdx, arr) => {
            let total = arr.reduce((a, c) => a + c, 0);

            if (curIdx >= nums.length) return
            
            if (total > target) return;

            if (total === target) {
                result.push([...arr]);
                return;
            }

       
            recursive(curIdx + 1, arr);
            recursive(curIdx, [...arr, nums[curIdx]]);
        };

        recursive(0, []);

        return result;
    }
}
