#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""

        """ Best case: 0(1) if the linked list only has one item.
        Worst case: 0(n) if linked list has n amount of items. """
        node = self.head

        count = 0
        while node is not None:
            count += 1
            node = node.next

        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""

        """ Best and Worst Case: O(1) because we are making a new node if the
            list is empty or going straight to the tail node and adding a new node
            after that. """

        new_node = Node(item)
        if self.tail is not None:

            #set current tail pointer to new node
            self.tail.next = new_node

            #point tail to new node
            self.tail = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""

        """ Best and Worst Case: 0(1) because we always start at the head node or
            initialize it. """

        new_node = Node(item)
        if self.head is not None:
            new_node.next = self.head

            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""

        """ Best case: 0(1) under the condition that the first node is what we
            are looking for or if there's only one item in the linked list
             Worst case: 0(n) under the condition that the nth node is what we are
             looking for. """

        node = self.head
        while node is not None:
            if quality(node.data) == True:
                return node.data
            else:
                node = node.next

        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        
        """ Best case: 0(1) under the condition that the first node is what we
            are "deleting" or if there's only one item in the linked list
            Worst case: 0(n) under the condition that the nth node is what we
            are "deleting"""

        current_node = self.head
        previous_node = None
        while current_node is not None:

            if item == current_node.data:

                if previous_node is None:

                    #make head the next node
                    self.head = current_node.next

                    #If head is also the tail
                    if current_node.next is None:
                        self.tail = previous_node

                #if item we want removed is the tail
                elif current_node.next is None:
                        previous_node.next = None
                        self.tail = previous_node

                else:
                    previous_node.next = current_node.next

                return

            else:
                previous_node = current_node
                current_node = current_node.next

        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
