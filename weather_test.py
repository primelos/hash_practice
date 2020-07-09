with open ('nyc_weather.csv', 'r') as f:
    arr = []
    for i in f:
        result = i.split(',')
        # print('result',result)
        try:
            temperature = int(result[1])
            # print('temperature',type(temperature))
            arr.append(temperature)
        except:
            print('not a valid temperature')
    # print(arr)
    
    
        
print('first seven days', sum(arr[0:7]) / len(arr[0:7]))
print('max temp', max(arr))

with open ('nyc_weather.csv', 'r') as g:
    dict = {}
    
    for j in g:
        # print(j)
        result2 = j.split(',')
        day = result2[0]
        # print('day', day)
        if j[0] == 'd':
            pass
        else:
            temp = int(result2[1])
            # print('temp', temp)
            dict[day] = temp
        
print(dict)
print('Jan 9:',dict['Jan 9'])
print('Jan 4:', dict['Jan 4'])