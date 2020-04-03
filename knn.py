import math
file = open("train_iris.txt","r")
store=[]
train=[]
kt=input('enter the value of k')
c1=[]
c=0.0
acc=0.0
for line in file:
    store = line.split()
    train.append(store)
file.close()
#print train
print'\n\n\n\n'
file=open("test_iris.txt","r")
test=[]
for line in file:
    store=line.split()
    test.append(store)
#print test
file.close()
#r=[0 for i in range(0,len(train))]
for i in range(0,len(test)):
    c1=[0,0,0]
    for j in range(0,len(train)):
        s=0.0
        for k in range(0,4): 
            s=s+pow((float(test[i][k])-float(train[j][k])),2)
        r = math.sqrt(s)
        train[j] = train[j] + [r]
    train.sort(key=lambda x: x[5])
    for j in range(0,kt):
        if(train[j][4]=='0'):
            c1[0]+=1
        elif(train[j][4]=='1'):
            c1[1]+=1
        else:
            c1[2]+=1
        #print c1
    #c=max(c1[0],c1[1],c1[2]);
    if(c1[0]>c1[1] and c1[0]>c1[2]):
        print 'setosa'
        test[i]=test[i]+[0]
    elif(c1[1]>c1[0] and c1[1]>c1[2]):
        print 'versicolor'
        test[i]=test[i]+[1]
    else:
        print 'verginica'
        test[i]=test[i]+[2]
    #print c1
    #print train
    for row in train:
        del row[5]
    print test[i]
    if(int(test[i][4])==test[i][5]):
        c+=1
        print c
acc=float((c/len(test))*100)
print c
print len(test)
print float(c/len(test))
print "ACCURACY(in %)="
print acc



    
