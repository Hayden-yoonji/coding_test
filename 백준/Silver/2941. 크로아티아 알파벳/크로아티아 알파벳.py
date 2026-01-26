word = input()
c_alphabet = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in c_alphabet:
    word = word.replace(i,'*')
print(len(word))