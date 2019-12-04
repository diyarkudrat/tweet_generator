#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        """ Running time: O(n) or O(b*l) where b = # of buckets and l = average
            number of key-value pairs in each bucket. This is because you traverse
            through every bucket and every item within the bucket."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        """ Running time: O(n) or O(b*l) where b = # of buckets and l = average
            number of key-value pairs in each bucket. Same reasoning as the
            keys method."""

        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        """ Running time: 0(n) or O(b*l). This is because not only are you
            traversing through each bucket, but you are also calling the
            LinkedList.item method where you traverse through all nodes in each
            bucket. """

        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        """ Running time: O(n) or O(b*l). This is because you are traversing
            through every item within a bucket."""

        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

        count = 0
        for bucket in self.buckets:
            for key, value in bucket.items():
                count += 1
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        """ Running time: O(n) where n is number of nodes in the bucket. We are
            not traversing through each bucket, we are directly going to the bucket
            that corresponds to the key. You are still traversing through the nodes
            in the bucket. Best case:O(1) where key is the head node. Worst case:
            O(n)."""

        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        data = bucket.find(lambda item: item[0] == key)

        return data is not None

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        """ Running time: O(l) where l = average amount of key-value pairs
            in each bucket. Best case is key is not found and raises a KeyError.
            There's a hidden cost of using the contains method which adds on
            O(n)."""

        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        node = bucket.find(lambda item: item[0] == key)

        if node is not None:
            return node[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        """ Running time: O(l) where l = average number of key-value pairs
            in a bucket. The method runtime increases with respect to the length
            of the bucket. The runtime for finding the bucket is constant because
            it uses the _bucket_index helper. Worst case is O(n) where n is the
            amount of nodes that is in the bucket. """

        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        node = bucket.find(lambda item: item[0] == key)

        if node is not None:
            bucket.delete(node)

        bucket.append((key, value))



    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        """ Running time: O(l) where l is the average amount of key-value pairs
            in a bucket. This is because the runtime only depends on one thing,
            which is the length of the one bucket it's traversing through.
            Best Case: O(1) where the key your're looking for is the head node.
            Worst Case: O(n) where n is the amount of nodes in the bucket."""

        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        node = bucket.find(lambda item: item[0] == key)

        if node is not None:
            bucket.delete(node)
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
