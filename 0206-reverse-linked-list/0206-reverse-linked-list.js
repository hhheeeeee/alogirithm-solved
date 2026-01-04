/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) { 
   let cur = head
   let prevNode = null
   while (cur != null) {
      let next = cur.next 
      cur.next= prevNode
      prevNode = cur 
      cur = next 
   }
   return prevNode
};
