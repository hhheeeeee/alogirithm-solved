/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    return [...BigInt(BigInt(digits.map((v) => String(v)).join('')) + 1n).toString()].map((v) => Number(v))
};