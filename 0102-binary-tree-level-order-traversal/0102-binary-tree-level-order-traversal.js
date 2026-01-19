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
 * @return {number[][]}
 */
var levelOrder = function (root) {
    let result = [];
    let level = 0;

    const recursion = function (node, level) {
        if (!node) return;

        if (!result[level]) {
            result.push([node.val]);
        } else {
            result[level].push(node.val);
        }

        recursion(node.left, level + 1);
        recursion(node.right, level + 1);
    }

    recursion(root, level);
    return result;
};