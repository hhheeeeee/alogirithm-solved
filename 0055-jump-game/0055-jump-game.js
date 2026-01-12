/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
    let reachable = new Array(nums.length).fill(0)

    let queue = [0]

    while (queue.length > 0) {
        let now = queue.shift()
        let dist = nums[now]
        for (let i = now; i < now + dist + 1; i++) {
            if (i < nums.length && reachable[i] === 0) {
                reachable[i] = 1
                queue.push(i)
            }
        }
    }
    return reachable[nums.length - 1] === 1
};