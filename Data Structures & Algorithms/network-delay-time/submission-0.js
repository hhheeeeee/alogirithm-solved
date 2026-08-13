class Solution {
    /**
     * @param {number[][]} times
     * @param {number} n
     * @param {number} k
     * @return {number}
     */
    networkDelayTime(times, n, k) {
        const graph = Array.from({ length: n + 1 }, () => []);

        for (const [start, end, cost] of times) {
            graph[start].push([end, cost]);
        }

        const dist = Array(n + 1).fill(Infinity);
        const visited = new Set();

        dist[k] = 0;

        while (visited.size < n) {
            let u = -1;

            for (let node = 1; node <= n; node++) {
                if (!visited.has(node) && (u === -1 || dist[node] < dist[u])) {
                    u = node;
                }
            }

            if (u === -1 || dist[u] === Infinity) {
                break;
            }

            visited.add(u);

            for (const [next, cost] of graph[u]) {
                dist[next] = Math.min(dist[next], dist[u] + cost);
            }
        }

        const answer = Math.max(...dist.slice(1));

        return answer === Infinity ? -1 : answer;
    }
}
