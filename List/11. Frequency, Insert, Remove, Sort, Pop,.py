# Frequency, Insert, Remove, Pop 

z = ["Ankit","Moon","Ankit","Moon","Moon","Sun"]


# 1. Printing the frequency of a word in list
print("Frequency of word Ankit = " , z.count("Ankit"))
print("Frequency of word Moon = " , z.count("Moon"))
print("Frequency of word Sun = " , z.count("Sun"))


# 2. Inserting element in the list
print("List before adding elements = " ,z)
z.insert(2,"Jupiter")
z.insert(3,"Monday")
print("New list after adding elements = " ,z)


# 3. Removing elements from the list
print("List before removing elements = " ,z)
z.remove("Jupiter")
z.remove("Monday")
print("New list after removing elements = " ,z)


# 4. Using pop function 
print("List before using pop function = " ,z)
p = z.pop()
print("New list after using pop function = " ,p)
