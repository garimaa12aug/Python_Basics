
#All in one program¶


# Importing libraries
import timeit

# Usage of builtin functions
start = timeit.default_timer()   

# Defining a list
array_list = [10,11,15,19,21,32]      
array_np_list = []

# Print the list
print("Original List",array_list,"\n")   

# Defining a function
def prime(num):      
    if num > 1:     
        
        # check for factors
        # Iterating a range of numbers
        for i in range(2,num):    
            if (num % i) == 0:
                
                # Appending data to list
                array_np_list.append(num)           
                print(num,"is not a prime number (",i,"times",num//i,"is",num,")")
                
                # Terminating a loop run
                break         
        else:
            print(num,"is a prime number")
            
# Iterating a list
for item in array_list:
    
    # Calling a function
    prime(item)         

print("\nNon-prime List",array_np_list,"\n")

end = timeit.default_timer()

# Computing running time
print("Time Taken to run the program:",end - start, "seconds")       


'''
output
Original List [10, 11, 15, 19, 21, 32] 

10 is not a prime number ( 2 times 5 is 10 )
11 is a prime number
15 is not a prime number ( 3 times 5 is 15 )
19 is a prime number
21 is not a prime number ( 3 times 7 is 21 )
32 is not a prime number ( 2 times 16 is 32 )

Non-prime List [10, 15, 21, 32] 

Time Taken to run the program: 0.02714430000014545 seconds

Note:¶

    Python is a procedural Language
    Two versions of Python 2 vs 3
    No braces. i.e. indentation
    No need to explicitly mention data type 
'''

