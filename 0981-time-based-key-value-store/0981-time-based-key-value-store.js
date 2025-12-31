
var TimeMap = function() {
    this.map = new Map();
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function (key, value, timestamp) {
  const arr = this.map.get(key);
  if (!arr) {
    this.map.set(key, [[value, timestamp]]);
    return;
  }
  arr.push([value, timestamp]);
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function (key, timestamp) {
  let values = this.map.get(key) ?? [];
  let [l, r, value] = [0, values.length - 1, ""];
  while (l <= r) {
    let mid = Math.floor((l + r) / 2);
    if (values[mid][1] <= timestamp) {
      value = values[mid][0];
      l = mid + 1;
    } else {
      r = mid - 1;
    }
  }
  return value;
};

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */