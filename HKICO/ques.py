print(ord('a'))

for d in 'abcd':
    print(ord(d))
    
print(sum([0, 1, 2, 3]))

# default param value
def hello(name='world!'):
    print('hello ' + name) 
    
hello('Nicky!')
hello()