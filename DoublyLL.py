class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


class DoublyCircularLinkedList:
    def __init__(self):
        # Initialize the dummy head node
        self.head = Node(-1)
        self.head.next = self.head
        self.head.prev = self.head

    # 1. Create a Linked List from an array
    def create_from_array(self, arr):
        for elem in arr:
            self.insert_at_end(elem)  

    # 2. Iterate the Linked List
    def iterate(self):
        current = self.head.next
        while current != self.head:
            print(current.elem, end=" -> ")
            current = current.next
        print("HEAD")

    # 3. Counting items
    def count(self):
        count=0
        temp= self.head.next
        while temp!= self.head:
            count+=1
            temp= temp.next
        return count

    # 4. Retriving node from an index
    def get_node(self, index):
        if index< 0:
            return None
        temp= self.head.next
        count= 0
        while temp!= self.head:
            if count == index:
                return temp
            count+=1
            temp= temp.next
        return None

    # 5a. Inseting node at the start
    def insert_at_start(self, elem):
        new_node= Node(elem)
        first= self.head.next
        new_node.next= first
        new_node.prev= self.head
        self.head.next= new_node
        first.prev= new_node

    # 5b. Inserting node at the end
    def insert_at_end(self, elem):
        new_node= Node(elem)
        last= self.head.prev
        new_node.next= self.head
        new_node.prev= last
        last.next= new_node
        self.head.prev= new_node

    # 5c. Inserting node at a specific index
    def insert_at_index(self, index, elem):
        if index < 0:
            return
        if index == 0:
            self.insert_at_start(elem)
            return
        temp= self.head.next
        current_index=0
        while temp != self.head:
            if current_index == index:
                new_node= Node(elem)
                prev_node= temp.prev
                new_node.next= temp
                new_node.prev= prev_node
                prev_node.next= new_node
                temp.prev= new_node
                return
            current_index+=1
            temp= temp.next
        if current_index == index:
            self.insert_at_end(elem)
# 6. Remove a node from the list
    def remove(self, index):
        if index < 0:
            return
        temp= self.head.next
        current_index=0
        while temp!= self.head:
            if current_index == index:
                prev_node= temp.prev
                next_node= temp.next
                prev_node.next= next_node
                next_node.prev= prev_node
                return
            current_index+=1
            temp= temp.next
        print("Index out of bounds. ")


# Main Method
if __name__ == "__main__":
    # Initialize the linked list
    linked_list = DoublyCircularLinkedList()

    # 1. Create from array
    print("Creating Linked List from array:")
    linked_list.create_from_array([10, 20, 30, 40, 50])
    linked_list.iterate()

    # 2. Count items
    print("\nCount of items in the list:")
    print(linked_list.count())

    # 3. Get node at index
    print("\nNode at index 2:")
    node = linked_list.get_node(2)
    if node:
        print(node.elem)

    # 4. Insert at start
    print("\nInserting 5 at the start:")
    linked_list.insert_at_start(5)
    linked_list.iterate()
    # 5. Insert at end
    print("\nInserting 60 at the end:")
    linked_list.insert_at_end(60)
    linked_list.iterate()
    # 6. Insert at index
    print("\nInserting 25 at index 3:")
    linked_list.insert_at_index(7, 25)
    linked_list.iterate()
    # 7. Remove node
    print("\nRemoving node at index 4:")
    linked_list.remove(4)
    linked_list.iterate()