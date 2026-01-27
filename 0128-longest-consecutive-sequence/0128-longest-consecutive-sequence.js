/**
 * @param {number[]} nums
 * @return {number}
 */

var longestConsecutive = function (nums) {
    let map = new Map()
    for (let i = 0; i < nums.length; i++) {
        map.set(nums[i], nums[i] + 1)
    }

    let max = 0
    for (let c of map.keys()) {
        if (map.get(c - 1) === undefined) {
            let now = map.get(c)
            let count = 0
            while (now !== undefined) {
                count += 1
                now = map.get(now)
            }
            max = Math.max(count, max)
        }
    }

    return max
};