/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {

    let result = false
    let prev = []

    const recursive = (num) => {
        let temp = 0;

        for (let c of String(num)) {
            temp += Number(c) ** 2
        };
        
        if (temp == 1) {
            result = true
            return;
        };

        if (prev.includes(temp)) {
            result = false
            return;
        };

        prev.push(temp)
        recursive(temp)
    }

    recursive(n)
    return result
};