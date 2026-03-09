/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function (gas, cost) {
    let n = gas.length


    for (let i = 0; i < n; i++) {
        if (i !== 0 && gas[i] - cost[i] <= 0) continue
        // i를 시작으로 잡고 사이클 돌기 시작
        let tank = gas[i]
        let now = i
        let startIndex = i
        let flag = 0
        for (let j = Math.floor((i + 1) % n); j <= Math.floor(i % n) + n; j++) {
            let next = Math.floor(j % n)
            if (tank - cost[now] < 0) {
                flag = 1
                break
            }
            tank = tank - cost[now] + gas[next]
            now = next
        }
        // break에 한번도 안걸렸을 때!
        if (flag == 0) return startIndex
    }

    return -1
};
