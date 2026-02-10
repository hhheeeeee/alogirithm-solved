/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
    // dp  f f f t f f f t 
    // s = l e e t c o d e

    let map = new Map()
    let dp = new Array(s.length).fill(0)

    for (let word of wordDict) {
        if (map.get(word[0])) {
            map.get(word[0]).push(word)
        } else {
            map.set(word[0], [word])
        }
    }

    let queue = []
    for (let val of map.get(s[0])) {
        queue.push([val, 0])
    }

    while (queue.length > 0) {
        let [cur, curIdx] = queue.pop()

        let lastIdx = cur.length + curIdx - 1
        if (lastIdx < s.length && dp[lastIdx] === 0 && s.slice(curIdx, lastIdx + 1) === cur) {
            dp[lastIdx] = 1
            let next = map.get(s[lastIdx + 1])
            if (next) {
                for (let nv of next) {
                    queue.push([nv, lastIdx + 1])
                }
            }
        }
    }


    return dp[s.length - 1]
};
