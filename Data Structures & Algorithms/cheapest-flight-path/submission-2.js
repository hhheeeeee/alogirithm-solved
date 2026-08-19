class Solution {
    /**
     * @param {number} n
     * @param {number[][]} flights
     * @param {number} src
     * @param {number} dst
     * @param {number} k
     * @return {number}
     */
    findCheapestPrice(n, flights, src, dst, k) {
        let graph = Array.from({ length: n + 1 }, () => []);

        for (let [s, e, cost] of flights) {
            graph[s].push([e, cost]);
        }

        let queue = [[src, 0, 0, new Set([src])]];
        let result = Infinity;

        while (queue.length > 0) {
            let [now, depth, cumCost, trace] = queue.pop();

            if (depth <= k + 1) {
                if (now === dst) {
                    result = Math.min(result, cumCost);
                }
            }

            if (depth > k + 1 || trace.size === n) continue;

            for (let [next, nc] of graph[now]) {
                if (!trace.has(next)) {
                    if (cumCost + nc > result) continue;
                    queue.push([next, depth + 1, cumCost + nc, new Set([...trace, next])]);
                }
            }
        }

        return result === Infinity ? -1 : result;
    }
}
