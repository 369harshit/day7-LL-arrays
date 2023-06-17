class Node: 
    def __init__(self, data):
          
        self.data = data 
        self.next = None
        self.random = None
        
        
def cloneLinkedList(head):
		
    # Initializing a temp pointer	
    temp = head
        
    # Interweaving the copy of nodes 
    while(temp):
        node = Node(temp.data)
        node.next = temp.next
        temp.next = node
        temp = temp.next.next
        
    # Initializing a temp pointer again
    temp = head

    # Adjusting the random pointers of copied values
    while(temp):
        if(temp.random):
            temp.next.random = temp.random.next
        temp = temp.next.next
    
    # Initializing a temp pointer again
    temp = head
    
    # Initializing head of the clone value
    clone = temp.next
    
    # separating both the lists
    while(temp.next):
        a = temp.next
        temp.next = temp.next.next
        temp = a
        
    return clone

# making linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Making random pointers
head.random = head.next.next
head.next.random = head
head.next.next.random = head.next

# Printing the linked list values
temp = head
print("Original Linked List is:")
while(temp):
    print("data:",temp.data, "random:",temp.random.data)
    temp = temp.next
    
# Printing the Cloned linked list values
temp = cloneLinkedList(head)
print()
print("Cloned Linked List is:")
while(temp):
    print("data:",temp.data, "random:",temp.random.data)
    temp = temp.next
