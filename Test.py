import collections

array = [1,2,3,2,2,2,3,2,2,3,2,2,3,3,1,1,1,1]
Counter = collections.Counter(array).most_common(1)[0][0]
print(Counter)

eins=0
zwei=0
drei=0
most_common=0
for i in array:
    if i==1:
        eins = eins+1
    elif i==2:
        zwei = zwei+1
    else:
        drei = drei+1

if eins>zwei and eins>drei:
    most_common = "eins"
elif zwei>drei and zwei>eins:
    most_common = "zwei"

