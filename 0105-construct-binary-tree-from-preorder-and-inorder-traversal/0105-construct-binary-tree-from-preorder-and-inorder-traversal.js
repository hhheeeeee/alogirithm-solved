/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {

    let index = 0
    let root = new TreeNode(preorder[0])

    const recursive = (node, s, e) => {
        if (s >= e) return node
        let mid =  inorder.indexOf(node.val)
        let left = inorder.slice(s, mid)

        if (left.length >= 1) {
            index += 1
            const next = new TreeNode(preorder[index])
            node.left = recursive(next, s, mid)
        } else {
            node.left = null
        }

        let right = inorder.slice(mid + 1, e)
        if (right.length >= 1) {
            index += 1
            const next = new TreeNode(preorder[index])
            node.right = recursive(next, mid + 1, e)
        } else {
            node.right = null
        }

        return node
    }

    recursive(root, 0, preorder.length)

    return root
};
