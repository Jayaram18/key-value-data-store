import threading 
#this is for python 3.0 and above. use import thread for python2.0 versions
from threading import*
import time

d={} #'d' is the dictionary to store data

#create operation 
#use syntax "create(key_name,value,timeout_value)"

def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") #error message-1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): #condition for file size less than 1GB and Json object value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #condition input key name capped at 32chars
                    d[key]=l
                else:
                    print("error: Key_name can contain only 32 characters")
            else:
                print("error: Memory limit exceeded!! ")#error message-2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message-3

#read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message-4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of Json Object i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message-5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message-4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message-5
        else:
            del d[key]
            print("key is successfully deleted")

#I have an additional operation of modify in order to change the value of key before its expiry time if provided

#modify operation 
#use syntax "modify(key_name,new_value)"

def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key") #error message-6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message-5
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") #error message-6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
