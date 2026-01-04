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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (root?.left == null && root?.right == null) {
        return root
    }
    
    let [curLeft, curRight] = [root.left, root.right]
    root.left = curRight
    root.right = curLeft
    invertTree(root.right)
    invertTree(root.left)
    return root
};