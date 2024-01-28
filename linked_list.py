
# Reverse a Linked List
def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Detect Cycle in a Linked List
def hasCycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Merge Two Sorted Lists
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

# Merge K Sorted Lists
def mergeKLists(lists: List[ListNode]) -> ListNode:
    nodes = []
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next
    nodes.sort()
    head = curr = ListNode(None)
    for node in nodes:
        curr.next = ListNode(node)
        curr = curr.next
    return head.next

# Detect Cycle in a Linked List II
def detectCycle(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow2 = head
            while slow != slow2:
                slow = slow.next
                slow2 = slow2.next
            return slow
    return None

# Remove Nth Node From End of List
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

# Reorder List
def reorderList(head: ListNode) -> None:
    if not head:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev, current = None, slow
    while current:
        current.next, prev, current = prev, current, current.next
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
