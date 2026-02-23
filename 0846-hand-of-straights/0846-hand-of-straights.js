/**
 * @param {number[]} hand
 * @param {number} groupSize
 * @return {boolean}
 */
var isNStraightHand = function (hand, groupSize) {
    // 하나의 그룹 사이즈가 groupSize 여야 한다는 뜻
    // [8,9,11] 3 ==> 그룹사이즈가 3이니까 3개씩 쪼갠다. 그럼 [8, 9, 11] 그룹사이즈 3인 그룹 1개 나옴 ==> false

    if (hand.length % groupSize !== 0) return false
    let memo = new Map()
    let 한그룹크기 = groupSize

    hand.sort((a, b) => a - b)

    for (let h of hand) {
        memo.get(h) ? memo.set(h, memo.get(h) + 1) : memo.set(h, 1)
    }

    for (let [key, value] of memo.entries()) {
        while (value > 0) {
            for (let i = key; i < key + 한그룹크기; i++) {
                let val = memo.get(i)
                if (val === undefined) {
                    return false
                } else if (val === 1) {
                    memo.delete(i)
                } else {
                    memo.set(i, val - 1)
                }
            }
            if (value > 0) {
                value--;
            }
        }
    }

    return memo.size > 0 ? false : true
}