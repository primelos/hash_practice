
with open('poem.txt', 'r') as p:
    count = {}
    for i in p:        
        words = i.split(' ')
        for j in words:
            j = j.replace('\n', '')
            j = j.replace('-', '')
            if j in count:
                count[j] += 1
            else:
                count[j] = 1    

print(count)   