# link of the question: https://leetcode.com/problems/add-two-numbers/description/

def addTwoNumbers(l1, l2):
    ans = ListNode(0)
    dummy = ans
    carry = 0
    while l1 or l2 or carry:
        total = 0
        if l1:
            total += l1.val
            l1 = l1.next
        
        if l2:
            total += l2.val
            l2 = l2.next
        
        dummy.next = ListNode( (total + carry) % 10 )
        dummy = dummy.next

        carry = (total + carry) // 10

    return ans.next