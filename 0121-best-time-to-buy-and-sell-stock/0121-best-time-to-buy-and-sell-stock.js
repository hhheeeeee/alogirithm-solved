/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let result = 0
  let cheapest = 10**4 + 1
  
  for (price of prices) {
    if (cheapest > price) {
        cheapest = price
        } else {
        result = Math.max(result, price - cheapest)
        }
    }

 return result
};

// 7 1 100