/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    let [left, right] = [0, nums.length - 1]
    // 어디쪽이 정렬되어 있는지 알아야됨 => 왼쪽인지 오른쪽인지

    while (left <= right) {
        let mid = Math.floor((left + right) / 2)
        if (nums[mid] === target) return mid
        if (nums[left] === target) return left
        if (nums[right] === target) return right
        console.log(left, right, mid)

        if (nums[left] > nums[mid]) { // 1) 오른쪽은 정렬된 상태
            if (nums[mid] < target && target < nums[right]) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        } else { // 2) 왼쪽은 정렬된 상태
            if (nums[left] < target && target < nums[mid]) { // 2-1) 정렬된 왼쪽 안에 타겟이 있음 
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
    }
    return -1
};