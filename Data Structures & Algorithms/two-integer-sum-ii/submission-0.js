class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let [s, e] = [0, numbers.length - 1];

        while (s < e) {
            let now = numbers[s] + numbers[e];
            if (now === target) {
                return [s + 1, e + 1];
            }
            if (now < target) {
                s += 1;
            } else {
                e -= 1;
            }
        }
        return [s + 1, e + 1];
    }
}