/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    const copy = matrix.map(v => [...v])
    const n = matrix.length
    for (i = 0; i < n ; i++) {
        for (j = n - 1; 0 <= j; j--) {
            matrix[i][n - j - 1] = copy[j][i]
        }
    }
};