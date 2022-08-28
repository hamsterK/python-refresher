# f strings
name = 'Bob'
print(f'Hello, {name}')

name = 'Rolf'
print(f'Hello, {name}')

# formatting
name = 'Bob'
greeting = 'Hello, {}'
with_name = greeting.format(name)
print(with_name)
print(greeting.format('Rolf'))

longer_phrase = 'Hello, {}. Today is {}.'
formatted = longer_phrase.format('Rolf', 'Monday')
print(formatted)
