class Solution {
    /**
     * @param {number[][]} heights
     * @return {number[][]}
     */
    pacificAtlantic(heights) {
        let result = [];
        let [toPacific, toAtlantic] = [false, false];
        let [colMax, rowMax] = [heights.length, heights[0].length];
        let dir = [[1, 0],[0, 1],[-1, 0],[0, -1]];
        let visited = Array.from({ length: colMax }, () => Array(rowMax).fill(0));

        function flow(col, row) {
            if (col === 0 || row === 0) {
                toPacific = true;
            }

            if (col === colMax - 1 || row === rowMax - 1) {
                toAtlantic = true;
            }

            if (toPacific && toAtlantic) return;

            visited[col][row] = 1;

            for (let [dx, dy] of dir) {
                let [ncol, nrow] = [col + dx, row + dy];
                if (0 <= ncol && ncol < colMax && 0 <= nrow && nrow < rowMax) {
                    if (visited[ncol][nrow] === 0 && heights[col][row] >= heights[ncol][nrow]) {
                        flow(ncol, nrow);
                    }
                }
            }

            return;
        }

        for (let col = 0; col < colMax; col++) {
            for (let row = 0; row < rowMax; row++) {
                toPacific = false;
                toAtlantic = false;
                visited = Array.from({ length: colMax }, () => Array(rowMax).fill(0));
                flow(col, row);
                if (toPacific && toAtlantic) {
                    result.push([col, row]);
                }
            }
        }

        return result;
    }
}
