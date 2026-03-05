/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function (n, flights, src, dst, k) {
    let graph = Array.from({ length: n }, () => [])

    for (let [from, to, cost] of flights) {
        graph[from].push([to, cost])
    }

    let best = Array.from({ length: n + 1 }, () => Array(n).fill(Infinity));
    best[0][src] = 0;

    let min = Infinity
    let queue = [[src, 0, 0]]
    while (queue.length > 0) {
        let [now, nowTotal, nowStop] = queue.pop()

        if (now == dst && nowStop <= k + 1) {
            min = Math.min(min, nowTotal)
            continue
        }

        if (nowTotal !== best[nowStop][now]) continue;
        if (nowTotal > min) continue;
        if (nowStop > k) continue;

        for (const [next, cost] of graph[now]) {
            const nextTotal = nowTotal + cost;
            const nextStop = nowStop + 1;

            if (nextTotal >= min) continue;

            if (nextTotal < best[nextStop][next]) {
                best[nextStop][next] = nextTotal;
                queue.push([next, nextTotal, nextStop]);
            }
        }

    }

    return min === Infinity ? -1 : min
};
