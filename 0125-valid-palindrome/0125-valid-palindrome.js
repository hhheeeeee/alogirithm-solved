/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // converting all uppercase letters into lowercase letters
    let lower = s.toLowerCase()
    // removing all non-alphanumeric characters
    let alphaOnly = [...lower].filter((char) => (char.charCodeAt() >= 65 && char.charCodeAt() <= 90) || (char.charCodeAt() >= 97 && char.charCodeAt() <= 122) || (char.charCodeAt() >= 48 && char.charCodeAt() <= 57))
    // backward reverse는 원본 배열을 뒤집지만, toReversed() 메서드는 reverse()에 대응되는 복사 메서드
    let backward = alphaOnly.toReversed((a, b) => b - a)
    
    console.log(alphaOnly)
    return JSON.stringify(alphaOnly) === JSON.stringify(backward);
};