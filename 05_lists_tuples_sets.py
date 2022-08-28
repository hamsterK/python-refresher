l = ['Bob', 'Rolf', 'Anne']  # list
t = ('Bob', 'Rolf', 'Anne')  # tuple: can't be modified
s = {'Bob', 'Rolf', 'Anne'}  # set: duplicates are impossible, no index

print(l[0])
print(t[1])

l[0] = 'Smith'
print(l[0])

l.append('Brown')
print(l[3])

l.remove('Rolf')
print(l)

s.add('Smith')
print(s)