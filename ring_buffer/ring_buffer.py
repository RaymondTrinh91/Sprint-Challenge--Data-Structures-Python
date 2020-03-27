from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If Ring Buffer is at capacity
        if self.storage.length == self.capacity:
            # If Pointer is at None
            # Start at Head
            if self.current == None:
                # Move Pointer to next node
                self.current = self.storage.head.next
                # Remove current head and replace
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
            # If Pointer is at tail
            elif self.current == self.storage.tail:
                # Move point back into position for Head
                self.current = None
                # Remove current tail and replace
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
            # Else Point is in middle of DLL
            else:
                # Set pointer to next node
                self.current = self.current.next
                # Remove previous node and replace
                self.current.prev.delete()
                self.current.insert_before(item)
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        
        node = self.storage.head

        while node:
            list_buffer_contents.append(node.value)
            node = node.next
        

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        if self.current < self.capacity - 1:
            self.current += 1
        else:
            self.current = 0

    def get(self):
        return [item for item in self.storage if item is not None]


