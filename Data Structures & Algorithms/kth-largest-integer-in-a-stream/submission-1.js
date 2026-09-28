class MinHeap {
    constructor() {
        this.heap = [];
    }

    length() {
        return this.heap.length;
    }

    peek() {
        return this.heap[0];
    }

    heapifyUp() {
        let currentIdx = this.length() - 1;

        while (0 < currentIdx) {
            let parentIdx = Math.floor((currentIdx - 1) / 2);

            if (this.heap[parentIdx] > this.heap[currentIdx]) {
                [this.heap[parentIdx], this.heap[currentIdx]] = [
                    this.heap[currentIdx],
                    this.heap[parentIdx],
                ];
                currentIdx = parentIdx;
            } else {
                break;
            }
        }
    }

    heapifyDown() {
        let currentIdx = 0;

        while (currentIdx < this.length()) {
            let leftChildIdx = currentIdx * 2 + 1;
            let rightChildIdx = (currentIdx + 1) * 2;
            let smallestIdx = currentIdx;
            if (this.heap[smallestIdx] > this.heap[leftChildIdx]) {
                smallestIdx = leftChildIdx;
            }

            if (this.heap[smallestIdx] > this.heap[rightChildIdx]) {
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
        return val;
    }
}

class KthLargest {
    /**
     * @param {number} k
     * @param {number[]} nums
     */
    constructor(k, nums) {
        this.heap = new MinHeap();
        this.k = k;

        for (let num of nums) {
            this.heap.push(num);
        }

        // 작은거 하나씩 빼서 딱 k개 남김
        while (this.heap.length() > this.k) {
            this.heap.pop();
        }
    }

    /**
     * @param {number} val
     * @return {number}
     */
    add(val) {
        this.heap.push(val);

        if (this.heap.length() > this.k) {
            this.heap.pop();
        }

        return this.heap.peek();
    }
}
