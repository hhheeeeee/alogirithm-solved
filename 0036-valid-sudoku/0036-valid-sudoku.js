/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {

    // rule 1
    for (i = 0; i < 9; i++) {
        let row = board[i].join('.').replaceAll('.', '').split('')
        let row_1 = new Set(row)
        if (row.length !== row_1.size) {
            return false
        }
        // rule 2
        let col = []
        for (let j = 0; j < 9; j++) {
            if (board[j][i] !== '.') {
                col.push(board[j][i])
            }
            // rule 3
            let grid = []
            if (i % 3 === 0 && j % 3 === 0) {
                let grid_1 = grid.concat(board[i].slice(j, j + 3), board[i + 1].slice(j, j + 3), board[i + 2].slice(j, j + 3))
                grid_1 = grid_1.join('.').replaceAll('.', '').split('')
                let grid_2 = new Set(grid_1)
                if (grid_1.length !== grid_2.size) {
                    return false
                }
            }
        }
        let col_1 = new Set(col)
        if (col.length !== col_1.size) return false
    }
    return true
};