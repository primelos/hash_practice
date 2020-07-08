my_table = {
    'march 2':320,
    'march 3':220,
    'march 4':340,
    'march 5':325,
    'march 6':395,
    'march 7':322,
    'march 8':376,
}

# def get_hash(key):
#     h=0
#     for char in key:
#         h += ord(char)
#     return h % 100

# print(get_hash('march 28'))

# print(my_table['march 4'])

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] =val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
# print(t.get_hash('march 6'))
t['march 6'] = 130
t['march 12'] = 140
t['march 15'] = 120

print(t.arr)
print('check', t['march 6'])
del t['march 6']
print(t.arr)