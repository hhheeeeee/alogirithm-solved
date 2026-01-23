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

    const recursive = (node, passed) => {
        if (!node || node.val == null) return;

        let goodFlag = true
        for (i = 0; i < passed.length; i++){
            if (passed[i] > node.val) {
                goodFlag = false
                break
            }
        }
        if (goodFlag){
            good += 1
        }
        recursive(node.left, [...passed, node.val])
        recursive(node.right, [...passed, node.val])
    }
    recursive(root, [])
    return good
};