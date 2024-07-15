from sys import stdin, stdout

word_list = set(stdin.readlines()[1:])

stdout.write(''.join(map(str,sorted(word_list, key=lambda x: (len(x), x)))))