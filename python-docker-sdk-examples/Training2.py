#!/usr/bin/env python

"""AsyncioEx.py: Demo code for Async IO"""
__author__ = "Sumit Kala"

import pdb
import time
import math

'''
Task:- ------- Given:- mesg="sample text was given to the program" 
Expected:- res="SamplE TexT WaS GiveN TO ThE PrograM" 
Hints: 
split for firschar = word[0] lastchar = word[-1] 
EF1 & EL1 = word[1:-1] 
convert the to upper & concat & Store them in new a list 
join new list Duration 
'''

'''
Sample 1


res="SamplE TexT WaS GiveN TO ThE PrograM"
mesg="sample text was given to the program"
x = mesg.split()
reslst = [w[0].upper()+w[1:-1]+w[-1].upper() for w in mesg.split()]
print(" ".join(reslst))
'''

# In place operation

alist = [1, 2, 3, 4, 5]
# Result:alist = [1,4,9,16,25] without chnaging id of alist
print(id(alist))
'''
Method 1
for i in range (len(alist)):
 alist[i]*=alist[i]

print(alist)
print(id(alist))
'''
'''
Method 2
alist[:] = [e*e for e in alist]
print(alist)
print(id(alist))
'''

'''
Task 2
mesg = "one-eight-nine-zero"
Expected 
res = "1890"

Sol 1

mesg = "one-eight-nine-zero"

dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
res = "".join(list(str(dict[e]) for e in mesg.split("-")))
print(res)
=======================
Sol 2
lst = mesg.split("-")
result=""
for e in lst:
 result += str(dict[e])
print(result)
'''

'''
Task 3
Task:- ======= fob = open("server.csv", "w") 
fob.write("name,ipv4,osname\n") 
fob.write("smtp,10.1.1.1,win2k\n") 
fob.write("dbserver,10.1.1.2,linux\n") 
fob.write("webserver,10.1.1.18,HPUX\n") 
fob.close() # prepare a nested dict out of this CSV File # 
pickle it & save it a file 
1) empty dict 
2) open the file & apply for 
3) split them 
4) add them to dict
 5) pickle it - save Duration : 10 mins Time : 12.40 to 11.50

'''
import pickle
'''
import pickle
import pprint
fob = open("server.csv", "w")
fob.write("name,ipv4,osname\n")
fob.write("smtp,10.1.1.1,win2k\n")
fob.write("dbserver,10.1.1.2,linux\n")
fob.write("webserver,10.1.1.18,HPUX\n")
fob.close()
with open("server.csv", "r") as fob:
 lab1,lab2,lab3 = fob.readline().rstrip("\n").split(",")
 print(lab1,lab2,lab3)
 adict={}
 for record in fob:
    name,ip,os = record.rstrip("\n").split(",")
    adict[name] = {}
    adict[name][lab2] = ip
    adict[name][lab3] = os
    pprint.pprint(adict)
    f1 = open("data.pkl", "wb")
    pickle.dump(adict, f1)
    f1.close()
'''

#Task 4
'''
contents of data.json:- -----------------------
{ "oper" : { "input" : "one.txt", "output" : "out.txt", "search" : "sample" } } 
Contents of one.txt:- 
---------------------- 
this is a sample text which is added using the editor sample data is appended to the file Expected output:- 
----------------- 
sample found 
'''
'''
#My solution
import json
fop = open("data.json","r")
oper = json.load(fop)
fop.close()
print(oper)
fop = open(oper['oper']['input'] ,"r")
line = fop.readline()
#pdb.set_trace()
fout = open(oper['oper']['output'],"w")
if line.find(oper['oper']['search']) == -1:
    fout.write("sample not found")
else:
    fout.write("sample found")
fout.close()

Sol 2

import json f1 = open("data.json") data = json.load(f1) f1.close() input_file = data["oper"]["input"] word_search = data["oper"]["search"].lower() output_file = data["oper"]["output"] f1 = open(input_file) strbuffer = f1.read().lower() out = open(output_file, "w") if word_search in strbuffer: out.write("%s Found" %(word_search)) else: out.write("%s Not Found" %(word_search)) f1.close() out.close()
'''
