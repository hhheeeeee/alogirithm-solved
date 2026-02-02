/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function (text1, text2) {
  const memo = Array.from({ length: text2.length + 1 }, () =>
    Array(text1.length + 1).fill(0)
  );

  for (let i = 1; i <= text2.length; i++) {
    for (let j = 1; j <= text1.length; j++) {   // 여기 j=1부터
      if (text1[j - 1] === text2[i - 1]) {
        memo[i][j] = memo[i - 1][j - 1] + 1;    // 여기 대각선 + 1
      } else {
        memo[i][j] = Math.max(memo[i][j - 1], memo[i - 1][j]);
      }
    }
  }

  return memo[text2.length][text1.length];
};

//    0 b s b i n i n m
// 0  0 0 0 0 0 0 0 0 0
// j  0 0 0 0 0 0 0 0 0
// m  0 0 0 0 0 0 0 0 1         
// j  0 0 0 0 0 0 0 0 1   
// k  0 0 0 0 0 0 0 0 1   
// b  
// k
// j
// k
// v


// 