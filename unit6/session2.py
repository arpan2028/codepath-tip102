class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def collect_false_evidence(evidence):
  loop = False
  result = {}
  slow = evidence
  fast = evidence
  visited = set()
  # node -> node -> null
  # Terminating statement would be when fast.next == null or fast.next.next == null
  while not fast == None and not fast.next == None:
    slow = slow.next
    fast = fast.next.next
    # if slow == fast return true
    if slow == fast:
      while not slow.value in visited:
        visited.add(slow.value)
        slow = slow.next
      break
  return [x for x in visited]