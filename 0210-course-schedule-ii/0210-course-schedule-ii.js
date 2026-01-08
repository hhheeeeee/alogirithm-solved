/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function (numCourses, prerequisites) {
    let inDegrees = new Array(numCourses).fill(0)
    let graph = Array.from({ length: numCourses }, () => [])
    let result = []

    for (const [next, prev] of prerequisites) {
        graph[prev].push(next)
        inDegrees[next] += 1
    }

    let queue = inDegrees.map((v, idx) => (v === 0 ? idx : null)).filter((x) => x !== null);

    while (queue.length) {
        let cur = queue.shift()
        result.push(cur)

        for (let next of graph[cur]) {
            inDegrees[next]--;
            if (inDegrees[next] === 0) {
                queue.push(next)
            }
        }
    }

    return result.length === numCourses ? result : []
};