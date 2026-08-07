class Solution {
    /**
     * @param {number[][]} matrix
     * @return {void}
     */
    rotate(matrix) {
        let N = matrix.length;
        let result = Array.from({ length: N }, () => new Array(N).fill(0));

        for (let i = 0; i < N; i++) {
            for (let j = 0; j < N; j++) {
                result[j][N - i - 1] = matrix[i][j];
            }
        }

        for (let i = 0; i < N; i++) {
            for (let j = 0; j < N; j++) {
                matrix[i][j] = result[i][j]
            }
        }

        return matrix
    }
}

// 00 01 02
// 10 11 12
// 20 21 22

// 20 10 00
// 21 11 01
// 22 12 02
