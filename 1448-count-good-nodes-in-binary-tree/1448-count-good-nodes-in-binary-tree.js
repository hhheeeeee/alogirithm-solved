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
 * @return {number}
 */
var goodNodes = function(root) {
    let good = 0

    const recursive = (node, max) => {
        if (!node || node.val == null) return;

        if (node.val >= max) {
            good += 1
            recursive(node.left, node.val)
            recursive(node.right, node.val)
        } else {
            recursive(node.left, max)
            recursive(node.right, max)
        }
        
    }
    recursive(root, -Infinity)
    return good
};