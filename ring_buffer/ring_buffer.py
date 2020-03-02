from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if storage is not at max capacity yet (length of storage less than capacity)
        if self.storage.length < self.capacity:
            # add item to the tail of the doubly linked list
            self.storage.add_to_tail(item)
            # so long as we're not at max capacity, the oldest node is going to be the head,
            # since we are appending nodes to the tail (FIFO) -> 
            # set current equal to head node of doubly linked list. this is now the current oldest node
            self.current = self.storage.head
        # else if storage is at max capacity 
        else:
            # overwrite the value of the current oldest node, set it equal to item
            self.current.value = item
            # set current equal to the next node in the list 
            # if the current oldest node is tail of DLL, 
            if self.current is self.storage.tail:
                # start from beginning of DLL again and set current = to head
                self.current = self.storage.head
            # else set current = current.next
            else : self.current = self.current.next



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
                
        # start at head of DLL, save head node to variable
        node = self.storage.head
        # so long as node is not none (this would imply that we've reached the end of the list because tail.next will be none), iterate over DLL 
        while node:
            # append value of current node to list_buffer_contents on each iteration
            list_buffer_contents.append(node.value)
            # set node = next node in DLL 
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # initialize current_oldest to be 0, 
        # much like above function using DLL where current is initialized to head of list, current is initalized to first element in list here
        self.current_oldest = 0
        # initialize storage to be list containing None * capacity
        self.storage = [None] * capacity

    def append(self, item):
        # if at max capacity, the index of the current_oldest element will be equal to the capacity
        if self.current_oldest == self.capacity:
            # set it to first element in list again
            self.current_oldest = 0
        # overwrite the value of the current_oldest element with item   
        self.storage[self.current_oldest] = item
        # next oldest element will be one to the RHS of current_oldest -> increment current_oldest by one 
        self.current_oldest  += 1  

    def get(self):
        # only return items in storage where value is not None
         return [item for item in self.storage if item is not None]
