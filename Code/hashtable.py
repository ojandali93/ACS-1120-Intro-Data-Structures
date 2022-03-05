#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        return hash(key) % len(self.buckets)

    def keys(self):
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        list_of_values = []
        for current_bucket in self.buckets:
            for key, value in current_bucket.items():
                list_of_values.append(value)
        return list_of_values

    def items(self):
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        counter = 0
        for current_bucket in self.buckets:
            for item in current_bucket.items():
                counter += 1
        return counter

    def contains(self, key):
        current_index = self._bucket_index(key)
        current_bucket = self.buckets[current_index]

        current_entry = current_bucket.find_if__matches(lambda entry: entry[0] == key)

        if current_entry:
            return True
        else:
            return False

    def get(self, key):
        current_index = self._bucket_index(key)
        current_bucket = self.buckets[current_index]

        current_entry = current_bucket.find_if__matches(lambda entry: entry[0] == key)

        if current_entry is not None:
            value = current_entry[1]
            return value
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        current_index = self._bucket_index(key)
        current_bucket = self.buckets[current_index]

        current_entry = current_bucket.find_if__matches(lambda entry: entry[0] == key)

        if current_entry:
            current_bucket.update([key, value])
        else:
            current_bucket.append([key, value])

    def delete(self, key):
        current_index = self._bucket_index(key)
        current_bucket = self.buckets[current_index]
        entry = current_bucket.find_if_matches(lambda entry: entry[0] == key)
        if entry:
            current_bucket.delete(entry)
        else:
            raise KeyError('Key not found: {}'.format(key))


if __name__ == '__main__':
    ht = HashTable()
    print('hash table: {}'.format(ht))
