/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
    let tmpStack = []
    let idxStack = []
    let result = []
    for (let i = temperatures.length - 1; 0 <= i; i--) {
        let now = temperatures[i]
        // 감소 순열이 될 때까지 pop해
        while (tmpStack[tmpStack.length - 1] <= now) {
            tmpStack.pop()
            idxStack.pop()
        }
        if (tmpStack.length === 0) {
            result.unshift(0)
        } else {
            result.unshift(idxStack[idxStack.length - 1] - i)
        }
        tmpStack.push(now)
        idxStack.push(i)
    }
    return result
};