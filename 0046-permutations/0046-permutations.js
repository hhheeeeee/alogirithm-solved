/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    let result = []

    const permuation = (cur) => {
        if (cur.length == nums.length) {
            result.push([...cur])
            return 
        }

        for (let i = 0; i < nums.length; i++) {
            if (cur.includes(nums[i])) continue
            cur.push(nums[i])
            permuation(cur)
            cur.pop()
        }
    }

    permuation([])
    return result
}