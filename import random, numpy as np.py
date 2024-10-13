import random, numpy as np
#Creating bogo count, the sorted_array boolean, and a random array
bogo_count = 0
array_random = np.random.randint(1,100,5)
sorted_array = False

#Check if sorted
def is_sorted(array):
    #Get length of array
    length_of_array = len(array)
    #Loop through array length, -1 since the last element cant compare array[length_of_array] > array[length_of_array + 1] or else we get out of bounds error
    for i in range(0,length_of_array - 1):
        if array[i] > array[i+1]: return False # Return false if array is not sorted
    return True

#Bogo sort the array
def bogo_sort(array):
    length_of_array = len(array)
    #Loop through array length
    for i in range(0, length_of_array):
        #Generate random index
        random_index = random.randint(0,length_of_array-1) 
        #Switch array indexes
        array[i],array[random_index] = array[random_index], array[i] 

#Loop until bogo sort actually sorts the array
while not sorted_array:
    #Increment the counter, and call the functions
    bogo_count += 1
    bogo_sort(array_random)
    sorted_array = is_sorted(array_random)


print(f"Sorted within {bogo_count} tries.")