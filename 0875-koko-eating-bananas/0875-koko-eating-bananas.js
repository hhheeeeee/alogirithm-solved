/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */

var minEatingSpeed = function (piles, h) { //[3,6,7,11] , 8 ==> 4
    // Hint: 
    // try binary searching over the solution space. 
    // Given a fixed speed k, it is easy to check if Koko can eat all the bananas within h hours. 
    // If it works for k, we recurse by setting right = k. Otherwise, we recurse by setting left = k+1.
    let [s, e] = [Math.min(...piles), Math.max(...piles) + 1]
    let minK = Infinity

    const search = (s, e) => {
        if (s >= e) return

        let nowK = Math.floor((s + e) / 2)
        let tempHour = 0
        for (let c of piles) {
            tempHour += Math.ceil(c / nowK)
            if (tempHour > h) {
                search(nowK + 1, e)
                return
            }
        }
        minK = Math.min(minK, nowK)
        search(s, nowK)
    }

    search(s, e)
    return minK

}