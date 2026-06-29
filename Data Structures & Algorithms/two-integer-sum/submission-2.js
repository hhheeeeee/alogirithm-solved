class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let newNums = nums.map((v, i) => [v, i]).sort((a, b) => a[0] - b[0])
        let [i, j, result] = [0, nums.length - 1, 0]
        console.log(newNums)

        while (i < j) {
            result = newNums[i][0] + newNums[j][0]
            if (result === target) {
                return [Math.min(newNums[i][1], newNums[j][1]), Math.max(newNums[i][1], newNums[j][1])]
            } else if (result < target) {
                i += 1
            } else {
                j -= 1
            }
        }
        return [i, j]
    }
}
