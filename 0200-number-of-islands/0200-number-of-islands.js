/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
    let islands = 0
    let [m, n] = [grid.length, grid[0].length]

    const dfs = (x, y) => {
        grid[x][y] = "2"
        let dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for (let [dx, dy] of dir) {
            let [nx, ny] = [x + dx, y + dy]
            if (0 <= nx && nx < m && 0 <= ny && ny < n && grid[nx][ny] == "1") {
                dfs(nx, ny)
            }
        }
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] == "1") {
                dfs(i, j)
                islands += 1
            }
        }
    }
    return islands
};