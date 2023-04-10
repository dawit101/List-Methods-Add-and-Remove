#List Methods


# ADDING METHODS
basket = [1,2,3,4,5]

basket.append(100) #append = add to end of list
newlist = basket
print(newlist) 

print('---------------')

cat = [1,2,3,4,5]
      #0,1,2,3,4    <-- Bookshelf

cat.insert(3, 100) #insert = insert object before index (index, object)
#Count the index like counting the bookshelf
newList = cat
print(newList) 

print('---------------')

dog = [1,2,3,4,5]
dog.extend([100, 101]) #Extend list by appending elements from the iterable.
a = dog
print(a) 

print('---------------')

# REMOVING METHODS

rat = [1,2,3,4,5]
      #0,1,2,3,4    <-- Bookshelf

rat.pop() #pops off last bookshelf number at end of the list
print(rat)
rat.pop(0) #pops the bookshelf number 0, which is 1
print(rat)

print('---------------')
q = [1,2,3,4,5]

q.remove(4) # remove = removes the actual value
print(q)

print('---------------')
qwe = [1,2,3,4,5]

qwe.clear() #clear = removes everything inside array
print(qwe)