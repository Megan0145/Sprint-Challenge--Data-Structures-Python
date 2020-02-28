class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED

    # start off at head of the list, declare variable to hold current node and initialize it to the head node
    cur_node = self.head
    # declare variable to hold the previous node and initialize it to None
    prev_node = None
    # iterate over the list so long as the current node is not None (this denotes that we've reached the end of the list because tail.next will be None)
    while cur_node: 
      # save the value of the current nodes 'next' to a temp next variable
      next_node = cur_node.get_next()     
      # set the current nodes 'next' to the value of prev 
      cur_node.set_next(prev_node)
      # set the value of prev equal to the value of the current node
      prev_node = cur_node
      # finally set the value of the current node equal to the value we saved in the temp 'next' variable
      cur_node = next_node
    # when we get to the very end of the list (cur_node is None) prev_node will be equal to original tail of DLL
    # set head == prev_node  
    self.head = prev_node      
