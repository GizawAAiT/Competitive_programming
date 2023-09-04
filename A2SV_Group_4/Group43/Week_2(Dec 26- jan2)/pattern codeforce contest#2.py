n = int(input())
words = []
for _ in range(n):
    words.append(input())

pattern = ''
# print(words)
for ind in range(len(words[0])):
    cur = '?'
    for word in words: 
        if cur =='?' and word[ind] != '?':
            cur = word[ind]  
        elif cur !='?' and word[ind] != '?' and word[ind] != cur:
            cur = ''
            break
    # print(((ind)), cur)
    if cur == '?': pattern += 'x'
    elif cur == '': pattern += '?'
    else: pattern += cur 
print(pattern)


