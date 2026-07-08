class MaxHeap {
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
            if (this.heap[parentIdx] >= this.heap[currentIdx]) break;
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
            let largestIdx = currentIdx;

            if (leftChildIdx < this.length() && this.heap[leftChildIdx] > this.heap[largestIdx]) {
                largestIdx = leftChildIdx;
            }

            if (rightChildIdx < this.length() && this.heap[rightChildIdx] > this.heap[largestIdx]) {
                largestIdx = rightChildIdx;
            }

            if (largestIdx === currentIdx) break;

            [this.heap[currentIdx], this.heap[largestIdx]] = [
                this.heap[largestIdx],
                this.heap[currentIdx],
            ];

            currentIdx = largestIdx;
        }
    }

    push(val) {
        this.heap.push(val);
        this.heapifyUp();
    }

    pop() {
        if (this.length() === 0) return undefined;
        if (this.length() === 1) return this.heap.pop();

        const max = this.heap[0];
        this.heap[0] = this.heap.pop();

        this.heapifyDown();

        return max;
    }

    peek() {
        return this.heap[0];
    }
}

class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        let maxHeap = new MaxHeap();

        for (let s of stones) {
            maxHeap.push(s);
        }

        while (maxHeap.length() >= 2) {
            let fst = maxHeap.pop();
            let snd = maxHeap.pop();
            if (fst === snd) continue;
            if (fst > snd) {
                maxHeap.push(fst - snd);
            }
        }

        if (maxHeap.length() === 0) return 0;
        return maxHeap.pop();
    }
}
