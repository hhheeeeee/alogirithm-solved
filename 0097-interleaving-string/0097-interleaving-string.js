var isInterleave = function (s1, s2, s3) {
  if (s1.length + s2.length !== s3.length) return false;

  const memo = Array.from({ length: s1.length + 1 }, () =>
    Array(s2.length + 1).fill(undefined)
  );

  const dfs = (p1, p2) => {
    if (memo[p1][p2] !== undefined) return memo[p1][p2];

    const k = p1 + p2; 

    if (p1 === s1.length && p2 === s2.length) {
      memo[p1][p2] = true;
      return true;
    }


    if (p1 < s1.length && s1[p1] === s3[k]) {
      if (dfs(p1 + 1, p2)) {
        memo[p1][p2] = true;
        return true;
      }
    }

    if (p2 < s2.length && s2[p2] === s3[k]) {
      if (dfs(p1, p2 + 1)) {
        memo[p1][p2] = true;
        return true;
      }
    }

    memo[p1][p2] = false;
    return false;
  };

  return dfs(0, 0);
};