/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function (k, nums) {
  this.kth = k;
  // 이진 트리를 기반으로 한 자료구조
  // 부모 노드가 자식들보다 작거나 같은 구조
  // 가장 작은 값이 부모 노드에 위치하는 자료구조
  this.minHeap = [];

  for (const num of nums) {
    this.push(num);
  }

  while (this.minHeap.length > this.kth) {
    this.pop();
  }
};

KthLargest.prototype.pop = function () {
  if (this.minHeap.length === 0) return undefined;
  if (this.minHeap.length === 1) return this.minHeap.pop();

  const smallest = this.minHeap[0];
  this.minHeap[0] = this.minHeap.pop(); 
  this.heapifyDown();                   
  return smallest;
};

KthLargest.prototype.push = function (val) {
  this.minHeap.push(val);
  this.heapifyUp();
};


KthLargest.prototype.heapifyUp = function () {
  let index = this.minHeap.length - 1;
  while (index > 0) {
    const parentIndex = Math.floor((index - 1) / 2);
    // 부모 인덱스에 있는 값이 더 작거나 같으면 종료
    if (this.minHeap[parentIndex] <= this.minHeap[index]) break;
    // 만약에 아니라면, 부모 노드와 현재 노드를 스왑
    [this.minHeap[parentIndex], this.minHeap[index]] = [
      this.minHeap[index],
      this.minHeap[parentIndex],
    ];
    index = parentIndex;
  }
};

KthLargest.prototype.heapifyDown = function () {
  let index = 0;
  while (index < this.minHeap.length) {
    let leftChildIndex = index * 2 + 1;
    let rightChildIndex = index * 2 + 2;
    let smallestIndex = index;
    // 왼쪽 자식이랑 오른쪽 자식이랑 비교해서 더 작은 자식이 smallestIndex가 됨
    if (
      leftChildIndex < this.minHeap.length &&
      this.minHeap[leftChildIndex] < this.minHeap[smallestIndex]
    ) {
      smallestIndex = leftChildIndex;
    }
    if (
      rightChildIndex < this.minHeap.length &&
      this.minHeap[rightChildIndex] < this.minHeap[smallestIndex]
    ) {
      smallestIndex = rightChildIndex;
    }
    // 만약에 자식들 중 더 작은 값이 없다면 종료
    if (smallestIndex === index) break;

    // 만약에 자식들 중 더 작은 값이 있다면, 부모 노드와 자식 노드를 스왑
    [this.minHeap[index], this.minHeap[smallestIndex]] = [
      this.minHeap[smallestIndex],
      this.minHeap[index],
    ];
    // 자식 노드로 이동
    index = smallestIndex;
  }
};


/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function (val) {
  this.push(val);

  if (this.minHeap.length > this.kth) {
    this.pop();
  }
  return this.minHeap[0];
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */


