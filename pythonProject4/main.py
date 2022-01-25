sample = {}
sample['a'] = 3
sample['b'] = 5
print(sample['a'])
print(sample['b'])
print(sample.get('c', -2))
print(sample.get('a', 10))
print(sample['a'] + sample['b'] + sample.get('c', -2) + sample.get('a', 10))
