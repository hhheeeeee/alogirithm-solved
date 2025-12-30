/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function (target, position, speed) {
  let fleet = 1;
  let arr = position
    .map((pos, index) => {
      return { pos, speed: speed[index], time: (target - pos) / speed[index] };
    })
    .sort((a, b) => b.pos - a.pos);

  console.log(arr);
  let peak = arr[0].time;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i].time > peak) {
      fleet++;
      peak = arr[i].time;
    }
  }
  return fleet;
};

