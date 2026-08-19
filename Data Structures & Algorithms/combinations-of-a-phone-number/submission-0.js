class Solution {
    /**
     * @param {string} digits
     * @return {string[]}
     */
    letterCombinations(digits) {
        let MAP = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        };

        let result = [];
        let N = digits.length;
        let temp = [];

        const backtrack = (num) => {
            
            if (num === N) {
                let word = temp.join("");
                word.length > 0 && result.push(word);
                return;
            }

            for (let i of MAP[digits[num]]) {
                temp.push(i);
                backtrack(num + 1);
                temp.pop(i);
            }
        };

        backtrack(0);
        console.log(result);
        return result;
    }
}
