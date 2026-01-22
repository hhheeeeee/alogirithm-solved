/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function (candidates, target) {
    candidates.sort((a, b) => a - b)
    let result = []
    let temp = []

    const backtrack = (now, currentSum) => {
        if (currentSum > target) return;

        if (currentSum === target) {
            result.push([...temp])
            return
        }
        let first = null
        for (let i = now; i < candidates.length; i++) {
            if (candidates[i] !== first) {
                temp.push(candidates[i])
                backtrack(i + 1, currentSum + candidates[i], candidates[i])
                first = temp.pop()
            }
        }

    }
    backtrack(0, 0)
    return result
}