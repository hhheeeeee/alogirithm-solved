class Solution {
    /**
     * @param {number[][]} grid
     */
    islandsAndTreasure(grid) {
        let N = grid.length;
        let M = grid[0].length;
        let dir = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ];

        let 보석들 = [];
        for (let i = 0; i < N; i++) {
            for (let j = 0; j < M; j++) {
                if (grid[i][j] == 0) {
                    보석들.push([i, j, 1]);
                }
            }
        }

        while (보석들.length > 0) {
            let [x, y, cost] = 보석들.shift();

            for (let [dx, dy] of dir) {
                let [nx, ny] = [x + dx, y + dy];
                if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                    if (grid[nx][ny] === 2147483647) {
                        console.log(nx, ny, cost);
                        grid[nx][ny] = cost;
                        보석들.push([nx, ny, cost + 1]);
                    }
                }
            }
        }

        return grid;
    }
}
