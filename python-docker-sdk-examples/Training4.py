from threading import Thread
from time import sleep

list1=[]
list2=[]
merge_list=[]
# function to create threads
def thread1():
    for i in range (1,6):
        list1.append(i)


        # wait 1 sec in between each thread
        sleep(1)

def thread2():
    for i in range(6, 11):
        list2.append(i)
        # wait 1 sec in between each thread
        sleep(2)

def thread3(lst):
    '''
    merge_list.append(list1)
    merge_list.append(list2)
    print("inside thread3")
    '''
    #lst[:] = list1+list2 OR as below
    lst+=list1
    lst+=list2



if __name__ == "__main__":
    thread_1 = Thread(target=thread1)
    thread_1.start()
    thread_1.join()
    print(list1)

    thread_2 = Thread(target=thread2)
    thread_2.start()
    thread_2.join()
    print(list2)

    thread_3 = Thread(target=thread3,args=(merge_list,))
    thread_3.start()
    thread_3.join()

    print(merge_list)
    print("thread finished...exiting")