class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let [s, e] = [0, nums.length];

        while (s < e) {
            let mid = Math.floor((s + e) / 2);
            if (nums[mid] === target) {
                return mid;
            }
            if (nums[s] === target) {
                return s;
            }
            if (nums[e] === target) {
                return e;
            }
            if (nums[mid] < target) {
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
        return -1;
    }
}
