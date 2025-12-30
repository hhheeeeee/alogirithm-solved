/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let stack = [];
  let dict = { "(": ")", "{": "}", "[": "]" };
  for (let char of [...s]) {
    if (Object.keys(dict).includes(char)) {
      stack.push(char);
    } else if (char === dict[stack[stack.length - 1]] && stack.length > 0) {
      stack.pop();
    } else {
        return false
    }
  }
  return stack.length === 0;
};