f_original = open("original.txt", 'r')
f_target = open("target.txt", 'r')

lines = ''.join(f_target.readlines()).split('\n\n')
print(lines)


f_original.close()
f_target.close()

# f_original = open("original.txt", 'w')
f_target = open("target.txt", 'w')

for idx, elem in enumerate(lines):
    f_target.write(f'{idx} {elem}\n')



f_original.close()
f_target.close()