
var Twitter = function () {
    this.feed = []
    this.myFolloing = new Map()
};


/**
 * @param {number} userId
 * @param {number} tweetId
 * @return {void}
 */
Twitter.prototype.postTweet = function (userId, tweetId) {
  this.feed.unshift([userId, tweetId]);
};

/**
 * @param {number} userId
 * @return {number[]}
 */
Twitter.prototype.getNewsFeed = function (userId) {
  const followingSet = this.myFolloing.get(userId) ?? new Set();

  return this.feed
    .filter(([v]) => v === userId || followingSet.has(v))
    .slice(0, 10)
    .map(([, tweetId]) => tweetId);
};

/**
 * @param {number} followerId
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.follow = function (followerId, followeeId) {
  if (!this.myFolloing.has(followerId)) {
    this.myFolloing.set(followerId, new Set());
  }
  this.myFolloing.get(followerId).add(followeeId);
};

/**
 * @param {number} followerId
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.unfollow = function (followerId, followeeId) {
  const set = this.myFolloing.get(followerId);
  if (!set) return;
  set.delete(followeeId);
};
/** 
 * Your Twitter object will be instantiated and called as such:
 * var obj = new Twitter()
 * obj.postTweet(userId,tweetId)
 * var param_2 = obj.getNewsFeed(userId)
 * obj.follow(followerId,followeeId)
 * obj.unfollow(followerId,followeeId)
 */