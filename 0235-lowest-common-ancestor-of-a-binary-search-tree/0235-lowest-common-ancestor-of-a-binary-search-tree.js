/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
    let large = p.val > q.val ? p : q
    let small = p.val > q.val ? q : p

    // large보다는 작아야되고, small보다는 작아야됨?
    let cur = root
    while (cur) {
        if (cur === small || cur === large) break  
        if (cur.val >= small.val && cur.val <= large.val) break 
        
        if (cur.val < small.val) {
            cur = cur.right
            continue
        }
        if (cur.val > large.val) {
            cur = cur.left
            continue
        }
    }

    return cur
};