/**
 * @param {number[][]} edges
 * @return {number[]}
 */
var findRedundantConnection = function (edges) {
    let root = new Array(edges.length + 1).fill(1).map((v, i) => v * i)
    let result

    let findParent = (v) => {
        if (v !== root[v]) {
            root[v] = findParent(root[v])
        }
        return root[v]
    }

    for (let [a, b] of edges) {
        let parentA = findParent(a)
        let parentB = findParent(b)
        if (parentA === parentB) { // 사이클 발생!
            result = [a, b]
        } else if (parentA > parentB) {
            root[parentA] = parentB
        } else {
            root[parentB] = parentA
        }
    }

    return result
}