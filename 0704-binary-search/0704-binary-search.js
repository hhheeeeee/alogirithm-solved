/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let [l, r] = [0, nums.length - 1]

    while (l <= r) {
        let mid = Math.floor((l + r) / 2)
        if (nums[mid] > target) {
            r = mid - 1
        } else if (nums[mid] < target) {
            l = mid + 1
        } else if (nums[mid] == target) {
            return mid
        }
    }
    return -1
};