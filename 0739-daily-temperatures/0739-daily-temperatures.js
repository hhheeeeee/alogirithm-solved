/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    let stack = []
    let idx = []
    let res = new Array(temperatures.length).fill(0)

    for (let i = temperatures.length - 1; i >= 0; i--) {
        let cur = temperatures[i]
        while (cur >= stack[stack.length - 1]) {
            stack.pop()
            idx.pop()
        }

        if (stack.length === 0) {
            res[i] = 0
        } else {
            res[i] = idx[idx.length - 1] - i
        }

        stack.push(cur)
        idx.push(i)
    }
    return res
};