/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[]}
     */
    rightSideView(root) {
        let result = [];

        let dfs = (node, depth) => {
            if (!node) return;

            if (result[depth] === undefined) {
                result.push(node.val);
            }

            if (node.right) {
                dfs(node.right, depth + 1);
            }

            if (node.left) {
                dfs(node.left, depth + 1);
            }
        };

        dfs(root, 0);
        return result;
    }
}
