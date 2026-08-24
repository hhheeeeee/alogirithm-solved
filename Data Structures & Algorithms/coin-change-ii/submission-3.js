class Solution {
    /**
     * @param {number} amount
     * @param {number[]} coins
     * @return {number}
     */
    change(amount, coins) {
        const memo = Array.from(
            { length: coins.length },
            () => new Array(amount + 1).fill(-1)
        );

        const recurse = (curIdx, curSum) => {
            if (curSum > amount) return 0;
            if (curSum === amount) return 1;

            if (memo[curIdx][curSum] !== -1) {
                return memo[curIdx][curSum];
            }

            let ways = 0;

            for (let i = curIdx; i < coins.length; i++) {
                ways += recurse(i, curSum + coins[i]);
            }

            memo[curIdx][curSum] = ways;
            return ways;
        };

        return recurse(0, 0);
    }
}