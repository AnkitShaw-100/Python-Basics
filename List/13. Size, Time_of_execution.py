# Size, time_of_execution
import sys
import timeit
list1 = [1,2,3,"Ankit","Shyam",True]
tuple1 = (1,2,3,"Ankit","Shyam",True)


print("Size of the list : ",sys.getsizeof(list1))
print("Size of the tuple : ",sys.getsizeof(tuple1))    


listtime = timeit.timeit(stmt = "[1,2,3,4,5]",number = 10000000)
tupletime = timeit.timeit(stmt = "(1,2,3,4,5)",number = 10000000)


print("List takes time : " ,listtime)
print("Tuple takes time : " ,tupletime)