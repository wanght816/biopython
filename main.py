import os
import abi
import sys
import os.path
import seq

def list_file(path):
    filelist= []
    for filename in os.listdir(path):
        if os.path.splitext(filename)[1] == '.ab1':
            filelist.append(filename)
    return filelist
            



if __name__=="__main__":

    folder = "C:\\Users\\wangh\\Desktop\\错义突变"
    file_list= list_file(folder)
    file_list.sort()
    trim_1 = 50
    trim_2 = 50
    ratio = 2
    interv = 7
    ignore = 40
    for file in file_list:
        (filename,xulie,list) = abi.panduan(file= folder+"\\"+file, trim_1=trim_1, trim_2=trim_2, ratio=ratio, interv=interv, ignore= ignore)
        (list_1 , n) = seq.contrast(xulie,trim_1,trim_2 )
        print(filename)
        print("纯合突变：", [i+n+1 for i in list_1])
        print("杂合突变：", [i+n for i in list])
