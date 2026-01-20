
/**
 * @param {number[][]} points
 * @return {number}
 */
var minCostConnectPoints = function (points) {
    let graph = []
    // 연결되어 있는지 아닌지 보기 위한 roots
    let roots = new Array(points.length).fill(1).map((v, i) => v * i)
    let minCost = 0

    // 점들끼리 모든 간선과 거리 구하기
    for (i = 0; i < points.length; i++) {
        for (j = i + 1; j < points.length; j++) {
            let dist = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1])
            graph.push([dist, i, j])
        }
    }

    graph.sort((a, b) => a[0] - b[0])

    const findParent = (x) => {
        if (x !== roots[x]) {
            roots[x] = findParent(roots[x])
        }
        return roots[x]
    }

    const union = (a, b) => {
        let parentA = findParent(a)
        let parentB = findParent(b)

        if (parentA > parentB) {
            roots[parentA] = parentB
        } else {
            roots[parentB] = parentA
        }
    }
    
    // kruscal로 찾기
    for (let i = 0; i < graph.length; i++) {
        [dist, s, e] = graph[i]
        if (findParent(s) !== findParent(e) ) {
            union(s, e)
            minCost += dist
        }
        
    }
    return minCost
};