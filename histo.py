def histogram(item):
    for n in item:
        output=''
        time = n
        while(time>0):
            output+="*"
            time= time-1
        print(output)
histogram([2,3,4,5])
