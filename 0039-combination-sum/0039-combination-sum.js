/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {

    let result = []

    const dfs = (current, start) => {
        let sum = current.reduce((prev, cur) => prev + cur, 0)
        
        if (sum == target) {
            result.push([...current])
            return 
        }

        if (sum > target) return

        for (let i = start ; i < candidates.length; i++) {
            current.push(candidates[i])
            dfs(current, i)
            current.pop()
        }
    } 

    dfs([], 0)

    return result
};
