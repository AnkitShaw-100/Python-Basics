# Longest word && Smallest Word
n =  input("Enter a String : ")
print(f"Entered String is {n}")
m = n.split()
print(f"String after Splitting {m}")
longnest_word = max(m,key=len)
print(longnest_word)
smallest_word = min(m,key=len)
print(smallest_word)