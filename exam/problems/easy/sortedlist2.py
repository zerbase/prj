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
        if head: 
            r_list = ListNode(head.val)
        else:
            return None

        r_head = r_list
        while head != None:
            if head.val != r_list.val:
                r_list.next = ListNode(head.val)
                r_list = r_list.next
           
            head = head.next
            
        
        return r_head

if __name__ == "__main__":

    sol = Solution()

    li = ListNode(1)
    li2 = ListNode(1)
    li3 = ListNode(2)
    li35 = ListNode(2)
    li4 = ListNode(3)
    li5 = ListNode(3)
    li6 = ListNode(3)

    li.next = li2
    li2.next = li3
    li3.next = li35
    li35.next = li4
    li4.next = li5
    li5.next = li6

    rtv = sol.deleteDuplicates(li)
    print('---------')
    while rtv !=None:
        print(rtv.val)
        rtv = rtv.next
            
        