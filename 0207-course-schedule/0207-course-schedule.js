/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
    // [[1,0]] 0 -> 1
    let indegree = new Array(numCourses).fill(0)
    let graph = Array.from({ length: numCourses }, () => [])
    for (const [e, s] of prerequisites) {
        indegree[e] += 1
        graph[s].push(e)
    }

    let queue = []

    for (let i = 0; i < numCourses; i++) {
        if (indegree[i] == 0) {
            queue.push(i)
        }
    }

    while (queue.length > 0) {
        let cur = queue.pop()
        for (let next of graph[cur]) {
            indegree[next] -= 1
            if (indegree[next] === 0) {
                queue.push(next)
            }
        }
    }
    // 모든 정점을 방문하기 전에 큐가 비게 된다면 사이클이 존재
    let result = indegree.every(v => v === 0)
    return result
};