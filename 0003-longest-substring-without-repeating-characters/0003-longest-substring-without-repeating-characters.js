
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    let result = 0; substr = []

    for (let i = 0; i < s.length; i++) {
        if (substr.includes(s[i])) {
            while (true) {
                let first = substr.shift()
                if (first === s[i]) {
                    break
                }
            }
        }
        substr.push(s[i])
        result = Math.max(result, substr.length)
    }
    return result
};