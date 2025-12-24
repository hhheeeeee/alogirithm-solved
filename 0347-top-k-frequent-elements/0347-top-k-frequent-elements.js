/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let dict = {}
    nums.map((x) => {
        if (dict[x]) {
            dict[x]++;
        } else {
            dict[x] = 1
        }
    })
    const keys = Object.entries(dict) // [ [ '1', 3 ], [ '2', 2 ] ]
    .sort((a, b) => b[1] - a[1])      // 큰거 순서대로 정렬
    .map(([key]) => Number(key))      // [ 1, 2 ]

    return keys.slice(0,k)
};