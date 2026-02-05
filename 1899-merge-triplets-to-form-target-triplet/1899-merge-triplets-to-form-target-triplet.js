/**
 * @param {number[][]} triplets
 * @param {number[]} target
 * @return {boolean}
 */
var mergeTriplets = function (triplets, target) {

    let [f1, f2, f3] = [false, false, false]

    for (let [x, y, z] of triplets) {
        if (x <= target[0] && y <= target[1] && z <= target[2]) {
            if (x == target[0]) {
                f1 = true
            }
            if (y == target[1]) {
                f2 = true
            }
            if (z == target[2]) {
                f3 = true
            }
        }
    } 
    return f1 === true && f2 ===true && f3 ===true
};