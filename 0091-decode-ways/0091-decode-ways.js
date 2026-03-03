/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
    const n = s.length;
    const memo = new Array(n + 1).fill(-1);

    const dfs = (idx) => {
        if (idx === n) return 1;

        if (s[idx] === '0') return 0;

        if (memo[idx] !== -1) return memo[idx]

        let ways = dfs(idx + 1);

        if (idx + 1 < n) {
            const double = Number(s[idx] + s[idx + 1])
            if (double >= 10 && double <= 26) {
                ways += dfs(idx + 2);
            }
        }

        memo[idx] = ways;
        return ways;
    };

    dfs(0)

    return memo[0] === -1 ? 0 : memo[0]
};