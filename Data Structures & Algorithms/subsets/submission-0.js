class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        let result = [];
        const temp = [];

        const dfs = (start) => {
            result.push(temp.slice());

            for (let i = start; i < nums.length; i++) {
                temp.push(nums[i]);
                dfs(i + 1);
                temp.pop();
            }
        };

        dfs(0);

        return result;
    }
}
