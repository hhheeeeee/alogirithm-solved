/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let origin = String(x)
    let result = 0
    let start = origin[0] === "-" ? 1 : 0
    let 자리수 = 1
    for (let i = start; i < origin.length; i++) {
        result += 자리수 * origin[i]
        자리수 *= 10
        if (result > 2 **31) return 0
    }

    return start === 1 ? -result : result
};