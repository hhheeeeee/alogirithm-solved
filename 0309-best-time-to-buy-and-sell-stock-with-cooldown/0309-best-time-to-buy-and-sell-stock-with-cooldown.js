/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    // 0 : buy  1 : sell   2 : cooldown
    const memo = Array.from({ length: prices.length }, () => new Array(3).fill(0));

    memo[0][0] = -prices[0]; // 첫번째 사기

    for (let day = 1; day < prices.length; day++) {
        for (let i = 0; i < 3; i++) {
            if (i == 0) { // buy : 그냥 아무것도 안하고 있기 or cooldown 이후 사기
                memo[day][i] = Math.max(memo[day - 1][0], memo[day - 1][2] - prices[day])
            }
            if (i == 1) { // sell 
                memo[day][i] = memo[day - 1][0] + prices[day]
            }
            if (i == 2) { // cooldown : sell 한 다음 cooldown 
                memo[day][i] = Math.max(memo[day - 1][1], memo[day - 1][2])
            }
        }
    }

    return Math.max(...memo[prices.length - 1])
};