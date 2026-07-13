class MinHeap {
    constructor() {
        this.heap = [];
    }

    length() {
        return this.heap.length;
    }

    heapifyUp() {
        let currentIdx = this.length() - 1;

        while (currentIdx > 0) {
            const parentIdx = Math.floor((currentIdx - 1) / 2);

            // dist 값 비교
            if (this.heap[parentIdx][0] <= this.heap[currentIdx][0]) {
                break;
            }

            [this.heap[parentIdx], this.heap[currentIdx]] = [
                this.heap[currentIdx],
                this.heap[parentIdx],
            ];

            currentIdx = parentIdx;
        }
    }

    heapifyDown() {
        let currentIdx = 0;

        while (true) {
            const leftChildIdx = currentIdx * 2 + 1;
            const rightChildIdx = currentIdx * 2 + 2;
            let smallestIdx = currentIdx;

            if (
                leftChildIdx < this.length() &&
                this.heap[leftChildIdx][0] < this.heap[smallestIdx][0]
            ) {
                smallestIdx = leftChildIdx;
            }

            if (
                rightChildIdx < this.length() &&
                this.heap[rightChildIdx][0] < this.heap[smallestIdx][0]
            ) {
                smallestIdx = rightChildIdx;
            }

            if (smallestIdx === currentIdx) {
                break;
            }

            [this.heap[currentIdx], this.heap[smallestIdx]] = [
                this.heap[smallestIdx],
                this.heap[currentIdx],
            ];

            currentIdx = smallestIdx;
        }
    }

    pop() {
        if (this.length() === 0) return undefined;
        if (this.length() === 1) return this.heap.pop();

        const minVal = this.heap[0];
        const last = this.heap.pop();

        this.heap[0] = last;
        this.heapifyDown();

        return minVal;
    }

    push(val) {
        this.heap.push(val);
        this.heapifyUp();
    }
}

class Solution {
    /**
     * @param {number[][]} points
     * @return {number}
     */
    minCostConnectPoints(points) {
        const n = points.length;
        
        function calculateDistance(p1, p2) {
            return Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1]);
        }

        const visited = new Array(n).fill(false);
        const minHeap = new MinHeap();
        let totalDistance = 0;
        let count = 0;

        minHeap.push([0, 0]);

        while (count < n) {
            const [dist, current] = minHeap.pop();

            if (visited[current]) {
                continue;
            }

            visited[current] = true;
            totalDistance += dist;
            count++;

            for (let next = 0; next < n; next++) {
                if (!visited[next]) {
                    const nextDist = calculateDistance(
                        points[current],
                        points[next],
                    );
                    minHeap.push([nextDist, next]);
                }
            }
        }

        return totalDistance;
    }
}
