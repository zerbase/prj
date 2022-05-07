# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r_list = ListNode(head.val)
        b_val = None
        
        while head != None:
            print(head.val)
            if head.val != r_list.val:
                r_list.next = head
            
            head = head.next
        
        # print(r_list)
        while r_list !=None:
            print(r_list.val)
            r_list = r_list.next
        
        return r_list

if __name__ == "__main__":

    sol = Solution()

    li = ListNode(1)
    li2 = ListNode(1)
    li3 = ListNode(2)

    li.next = li2
    li2.next = li3

    sol.deleteDuplicates(li)
            
            
        