var search = function (nums, target) {
    function binary(nums, target, s, e) {
        if (s > e) return -1;
        let mid = Math.floor(s + (e - s) / 2);

        if (nums[mid] === target) return mid;

        if (nums[mid] >= nums[s]) {
            if (target >= nums[s] && target <= nums[mid])
                return binary(nums, target, s, mid - 1);
            else
                return binary(nums, target, mid + 1, e);
        } else {
            if (target >= nums[mid] && target <= nums[e])
                return binary(nums, target, mid + 1, e);
            else
                return binary(nums, target, s, mid - 1);
        }
    }

    return binary(nums, target, 0, nums.length - 1);
};