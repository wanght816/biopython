import os
import sys
import os.path
import matplotlib.pyplot as plt

def contrast(xulie, trim_1, trim_2):
    f = open(r"C:\Users\wangh\Desktop\错义突变\F4 #3.seq" ,"r")
    ref = f.read()
    n = 0
    count = 0
    list = []
    while n<= len(ref) - len(xulie)-1:
        #print(count, n)
        count = 0
        i = 0
        n += 1
        while i <= len(xulie) - 1:
            if ref[i+n] == xulie[i]:
                count += 1
            i += 1
        list.append(count)

    list1 = []
    list2 = []
    i=0
    n=list.index(max(list))+1
    while i <= len(xulie) - 1:
        if ref[i + n] != xulie[i] and i>trim_1 and i<len(xulie)-trim_2:
            list1.append(i)
            list2.append(xulie[i])
        i += 1


    #print(list1, list2, n, xulie[295:305],ref[295+n:305+n])
    return (list1,n)



