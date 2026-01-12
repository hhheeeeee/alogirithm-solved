/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
  let maxReach = 0;

  for (let i = 0; i < nums.length; i++) {
    if (i > maxReach) return false;          // 여기 못 오면 끝
    maxReach = Math.max(maxReach, i + nums[i]);
    if (maxReach >= nums.length - 1) return true; // 이미 끝 도달 가능
  }

  return true;
};