title = "First " 'Second ' "Third"
print(title)

s = 'a\0b\0c'
print(s, len(s))

s = '\001\002\x03'
print(s, len(s))

path = r"C:\py\code"
print(path)

myfile = open(r'D:\Python lessons\Marl_Luts\String Lesson.txt', 'w')
myfile.write(f'{path}')
myfile.close()

print(open(r'D:\Python lessons\Marl_Luts\String Lesson.txt').read())

print('-' * 158)

job = 'hacker'
for c in job: print(c, end=' ')
print('k' in job)

S = 'spam'
print(S[0], S[-1], S[1:3], S[1:], S[:-1])

S = 'abcdefghijklmnop'
print(S[9:1:-1])

S = '42'
I = 1
print(int(S) + I, S + str(I))
text = "1.234E-10"
print(float(text))

print(ord('s'), chr(115))

B = '1101'
I = 0
print(int(B, 2), bin(13))
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]
print(I)

S = 'spam'
S = S + 'SPAM!'
S = S[:4] + 'Burger' + S[-1]
print(S)

S = 'splot'
S = S.replace('pl', 'pamal')
print(S)

S = 'spammy'
S = S[:3] + 'xx' + S[5:]
print(S)
S = S.replace('mm', 'xx', 1)
print(S)
L = list(S)
L[3] = 'm'
L[4] = 'm'
S = ''.join(L)
print('middle = {0}'.format(L[3:5]))
print('{0:>10} = {1:<10}'.format('spam', 123.4567))
print('{:06.3f}'.format(3.14159))
print('{0:X}, {0:o}, {0:b}'.format(255))
print(f'{999999999999:,d}')