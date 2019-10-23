# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:56:55 2019

@author: tanuj
"""

l = eval(input('Enter number in list : '))

print('a) Total number of items in list :',len(l))

print('b) Fourth item in list :',l[3])

print('c) Last 3 items in list :',l[-3:])

print('d) All elements except first 2 :',l[2:])

l.reverse()
print('e) List in reverse order :',l)

print('f) Largest element = {0} and Smallest element = {1}'.format(max(l),min(l)))

if 5 in l:
    print('g) Yes, List contains 5 ')
else:
    print('g) No, List does not contains 5')

print('h) Total number of 5 in list :',l.count(5))

print('i) Sum of items in list :',sum(l))

del l[-1]
print('j) List after deleting the last item',l)

n = int(input('Enter a new number to replace with 2nd last item : '))
l[-2] = n
print('k) After changing the second last item :',l)

l.sort(reverse=True)
print('l) Sort the element in a reverse order :',l)

n = int(input('Enter number to delete from list : '))
if l.count(n)>0:
    l.remove(n)
    print('m) Delete the first occurence of an element')
else:
    print('m) The number is not in the list')
print('New List : ',l)

print('n) Perforn pop operation :',l.pop(2))