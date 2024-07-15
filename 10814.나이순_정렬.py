from sys import stdin, stdout

# First
# members = []
# inputs = stdin.readlines()
# for idx, i in enumerate(inputs[1:]):
#     members.append([idx,int(i.split()[0]),i.split()[1]])
# result = list(sorted(members, key= lambda x: (x[1],x[0])))

# for i in range(int(inputs[0])):
#     print(result[i][1],result[i][2])
    
# Second

stdout.write('\n'.join(map(str,sorted(stdin.read().splitlines()[1:],key=lambda id: int(id.split()[0])))))