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

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
