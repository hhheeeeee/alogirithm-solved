class Solution {
    /**
     * @param {number[]} cost
     * @return {number}
     */
    minCostClimbingStairs(cost) {
        let memo = new Array(cost.length + 1).fill(Infinity)

        memo[0] = 0
        memo[1] = 0
        
        for (let i = 2; i < cost.length + 1; i++) {
            memo[i] = Math.min(memo[i-1] + cost[i - 1], memo[i-2] + cost[i - 2])
        }

        return memo[cost.length]
    }
}
