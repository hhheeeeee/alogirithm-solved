/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function (cost) {
    const n = cost.length;
    let first = cost[0]
    let second = cost[1]

    if (n <= 2) return Math.min(first, second)
  
    for (let i = 2; i < n; i++) {
		let cur = cost[i] + Math.min(first, second);
		first = second;
		second = cur;
	}
	return Math.min(first, second);
  };