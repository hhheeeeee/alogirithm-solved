/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function (n, flights, src, dst, k) {
    let INF = Infinity
    let dist = Array(n).fill(INF);
    dist[src] = 0;

    for (let i = 0; i <= k; i++) { // 총 k+1번 완화
        const next = dist.slice();
        for (const [u, v, w] of flights) {
            if (dist[u] === INF) continue;
            const cand = dist[u] + w;
            if (cand < next[v]) next[v] = cand;
        }
        dist = next;
    }

    return dist[dst] >= INF ? -1 : dist[dst];
};
