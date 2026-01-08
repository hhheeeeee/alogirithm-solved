class minheap {
    constructor() {
        this.heap = [];
    }

    length() {
        return this.heap.length
    }

    heapifyUp() {
        let current = this.heap.length - 1

        while (current > 0) {
            let parentIndex = Math.floor((current - 1) / 2)
            if (this.heap[parentIndex][1] > this.heap[current][1]) {
                [this.heap[parentIndex], this.heap[current]] = [this.heap[current], this.heap[parentIndex]]
                current = parentIndex
            } else {
                break
            }
        }
    }

    heapifyDown() {
        let length = this.heap.length
        let index = 0

        while (true) {
            let smallestIndex = index
            let leftChildIndex = index * 2 + 1
            if (leftChildIndex < length && this.heap[leftChildIndex][1] < this.heap[smallestIndex][1]) {
                smallestIndex = leftChildIndex
            }
            let rightChildINdex = index * 2 + 2
            if (rightChildINdex < length && this.heap[rightChildINdex][1] < this.heap[smallestIndex][1]) {
                smallestIndex = rightChildINdex
            }

            if (smallestIndex == index) break;

            [this.heap[smallestIndex], this.heap[index]] = [this.heap[index], this.heap[smallestIndex]];
            index = smallestIndex
        }

    }

    push(val) {
        this.heap.push(val)
        this.heapifyUp()
    }

    pop() {
        if (this.heap.length <= 0) return undefined
        if (this.heap.length === 1) return this.heap.pop()
        let smallest = this.heap[0]
        this.heap[0] = this.heap.pop()
        this.heapifyDown()
        return smallest

    }
}

/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var networkDelayTime = function (times, n, k) {
    const graph = Array.from({ length: n + 1 }, () => [])

    for (const [s, e, time] of times) {
        graph[s].push([e, time])
    }

    let totalTime = new Array(n + 1).fill(Infinity)
    let queue = new minheap()
    totalTime[k] = 0
    queue.push([k, 0])

    while (queue.length() > 0) {
        let [now, nowTime] = queue.pop()

        // 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드
        if (totalTime[now] < nowTime) continue

        // 지금 나로부터 갈 수 있는 애들
        for (let [next, nextTime] of graph[now]) {
            if (nowTime + nextTime < totalTime[next]) {
                totalTime[next] = nowTime + nextTime
                queue.push([next, nowTime + nextTime])
            }
        }
    }

    // 0번째 빼고 나머지들 중에 time이 제일 큰 값 찾기
    let arr = totalTime.slice(1, n + 1)
    let max = Math.max(...arr)
    return max == Infinity ? -1 : max
}
