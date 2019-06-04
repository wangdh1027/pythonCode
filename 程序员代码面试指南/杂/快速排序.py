# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:01:54 2019

@author: comnet
"""
def part(arr,start,end):
    res = start
    while 1:
        while arr[end]>=arr[res] and end>start:
            end-=1
        if end == start:
            break
        start+=1
        while arr[start]<=arr[res] and start!=end:
            start+=1
        print(start,end)
        if start!=end:
            arr[start],arr[end] = arr[end],arr[start]
        else:
            arr[start],arr[res] = arr[res],arr[start]
            break
    return start
def kuaipai(arr,start,end):
    if start==end:
        return
    index = part(arr,start,end)
    print(arr)
    if index>start:
        kuaipai(arr,start,index-1)
    if index<end:
        kuaipai(arr,index+1,end)
#arr = [7,4,3,6,11,4,5,8]
#kuaipai(arr,0,len(arr)-1)


def QuickSort(myList,start,end):
    if start < end:
        i,j = start,end
        base = myList[i]
        while i < j:
            while (i < j) and (myList[j] >= base):
                j = j - 1
            myList[i] = myList[j]
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        myList[i] = base

        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList

def quicksort(List,start,end):
    if start<end:
        i,j = start,end
        base = List[i]
        while i<j:
            while i<j and List[j]>=base:
                j-=1
            while i<j and List[i]<=base:
                i+=1
            List[i],List[j] = List[j],List[i]
        List[start],List[j] = List[j],List[start]
        quicksort(List,start,i-1)
        quicksort(List,j+1,end)
    return List
myList = [12,3,4,5,38,65,97,76,13,3123,12312.4,13,412,31,3123,13,49]
print("Quick Sort: ")
quicksort(myList,0,len(myList)-1)
print(myList)

        
        
