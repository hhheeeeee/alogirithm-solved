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
 * @return {number[]}
 */
var rightSideView = function (root) {
    let queue = [[root, 0]]
    let result = []
    while (queue.length > 0) {
        let [node, depth] = queue.pop()
        if (node) {
            if (result.length <= depth) {
                result.push(node.val)

            }
            node.left && queue.push([node.left, depth + 1])
            node.right && queue.push([node.right, depth + 1])
        }
    }

    return result
};