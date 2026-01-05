function binSearch(array, term, comparator = (a, b) => a - b) {
  let lo = 0;
  let hi = array.length - 1;
  while (lo <= hi) {
    let mid = Math.floor((hi + lo) / 2);
    let comp = comparator(array[mid], term);
    if (comp < 0) {
      lo = mid + 1;
    } else if (comp > 0) {
      hi = mid - 1;
    } else {
      // found, return the index
      return mid;
    }
  }
  // not found, return the index at which the value should be
  return lo;
}


/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function KthLargest(k, nums) {
  this.k = k;
  this.nums = [];

  // insert all the elements
  while (nums.length) {
    this.add(nums.pop());
  }
};


/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function (val) {
  const idx = binSearch(this.nums, val);

  // insert element
  this.nums.splice(idx, 0, val);

  // remove leftmost element if window is larger than k
  if (this.nums.length === this.k + 1) {
    this.nums.shift();
  }

  // the first element is the element at k
  // if there are less than k elements we return the closest one
  return this.nums[0];
};
 

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */