import sys

sents = sys.stdin.read().splitlines()
for a_sent in sents:
    queue = []
    if a_sent == '.':
        break
    else:
        for i in a_sent:
            if i == '(':
                queue.append(i)
            elif i == '[':
                queue.append(i)
            elif i == ')' or i == ']':
                if not queue:
                    print('no')
                    break
                if i == ')':
                    if queue[-1] == '(':
                        queue.pop()
                    else:
                        print('no')
                        break
                if i == ']':
                    if queue[-1] == '[':
                        queue.pop()
                    else:
                        print('no')
                        break
            elif i == '.':
                if queue:
                    print('no') 
                else:
                    print('yes')
        