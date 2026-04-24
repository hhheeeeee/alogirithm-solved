/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
    const row = board.length
    const col = board[0].length

    const range = (x, y) => {
        return 0 <= x && x < row && 0 <= y && y < col
    }

    const search = (i, j, visited, depth) => {
        if (depth === word.length) {
            return true
        }

        const next = [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]

        for (const [nx, ny] of next) {
            if (range(nx, ny) && visited[nx][ny] === 0 && board[nx][ny] === word[depth]) {
                visited[nx][ny] = 1
                if (search(nx, ny, visited, depth + 1)) {
                    return true
                }
                visited[nx][ny] = 0
            }
        }

        return false
    }

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (board[i][j] === word[0]) {
                const visited = Array.from({ length: row }, () => new Array(col).fill(0))
                visited[i][j] = 1
                if (search(i, j, visited, 1)) {
                    return true
                }
            }
        }
    }

    return false
}