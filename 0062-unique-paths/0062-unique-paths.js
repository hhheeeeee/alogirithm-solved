/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {

    let dp = Array.from({ length: m }, () => Array.from({ length: n }, () => []))

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 1
            } else {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                console.log(dp, i, j)
            }
        }
    }

    return dp[m - 1][n - 1]
};