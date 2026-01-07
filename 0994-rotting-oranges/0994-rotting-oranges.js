var inRange = function (x, y, col, row) {
    if (0 <= x && x < col && 0 <= y && y < row) {
        return true
    }
    return false
}

/**
 * @param {number[][]} grid
 * @return {number}
 */
// 0 : empty, 1 : fresh,  2 : rotten
var orangesRotting = function (grid) {
    const dir = [[1, 0], [-1, 0], [0, -1], [0, 1]] // 4개 방향
    let minutes = 0
    let rotten = []

    let colLen = grid.length
    let rowLen = grid[0].length


    for (let i = 0; i < colLen; i++) {
        for (let j = 0; j < rowLen; j++) {
            if (grid[i][j] === 2) {
                rotten.push([i, j])
            }
        }
    }

    while (true) {
        let newRotten = []
        for (const [x, y] of rotten) {
            for (const [dx, dy] of dir) {
                let [nx, ny] = [x + dx, y + dy]
                if (inRange(nx, ny, colLen, rowLen)) {
                    if (grid[nx][ny] == 1) { // fresh 발견!
                        grid[nx][ny] = 2
                        newRotten.push([nx, ny])
                    }
                }
            }
        }
        if (newRotten.length === 0) break
        rotten = [...newRotten]
        minutes++
    };

    for (let i = 0; i < colLen; i++) {
        for (let j = 0; j < rowLen; j++) {
            if (grid[i][j] === 1) {
                return -1
            }
        }
    }

    return minutes
}