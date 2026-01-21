/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {

    let queue = [[root, -Infinity, Infinity]];

    while (queue.length > 0) {
        let [cur, min, max] = queue.shift()

        if (cur) {
            if (cur.right) {
                const v = cur.right.val
                if (v !== null && v !== undefined && v > cur.val && v < max) { // 아무리 왼쪽이라도 이거보단 커야대
                    queue.push([cur.right, Math.max(min, cur.val),  max])
                } else {
                    return false
                }
            }
            if (cur.left) {
                const v = cur.left.val;
                if (v !== null && v !== undefined && v < cur.val && v > min) {
                    queue.push([cur.left, min, Math.min(max, cur.val)]);
                } else {
                    return false;
                }
            }
        } else {
            continue
        }
    }
    return true

}
