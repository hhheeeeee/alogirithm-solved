/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function(k, nums) {
    this.kth  = k
    this.arr = nums.toSorted((a, b) => b - a)
    if (this.arr.length >= k) {
        this.arr = this.arr.slice(0, this.kth)
    }
};





// 8, 5, 4

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
   if (this.arr.length < this.kth) {
    this.arr.push(val)
    this.arr.sort((a, b) => b - a)
   } else {
    if (this.arr[this.kth - 1] < val) {
      this.arr.pop()
      this.arr.push(val)
      this.arr.sort((a, b) => b - a)
    }
   }
   return this.arr[this.kth - 1]
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */


