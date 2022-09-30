#I received no asistance on this assignment that violates the ethical guidelines set forth by the professor and the class syllabus 
#function 1 - done
def even_divide_count(num1, num2):
	#dividing num1 by num2 to get the intial value 
    remainder = int(num1/num2)
    if remainder % 2 == 0 and remainder > 0:
    	#using a built in counter in recursive function to figure out how many times number can be divided 
        return 1 + even_divide_count(remainder, num2)
    else:
        return 0
#print(even_divide_count(13,2))
#print(even_divide_count(9,3))
#print(even_divide_count(24,3))

#function2 
def add_sum(xs, ys):
	#checking to see if length works with function
    if len(xs) == 0:
        return ys
    else:
    	#using sum function to add all the items in each element 
        total = sum(xs[0])
        #appending to list 
        ys.append(total)
        #using recursion to get the sums of all elements and add them to the list 
        return add_sum(xs[1:], ys)


#print(add_sum([[1,2,3], [4,5,6], [7,8,9,10]], [3,4,5]))
#print(add_sum([[1,2,3], [4,5,6], [7,8,9,10]], []))
#print(add_sum([[]], [3,4,5]))
#print(add_sum([], [3,4,5]))



#function3 - done 
def swap_chars(str1, str2, n):
	#if the length of each string is less than n, return just the strings because nothing can be swapped 
    if len(str1) < n or len(str2) < n:
        return (str1, str2)
    else:
    	# swapping the characters in both strings based on n using slicing 
        part1 = str1[0:n-1] + str2[n-1]
        part2 = str2[0:n-1] + str1[n-1]
        #using recursive function to repeat the process for all characters 
        output = swap_chars(str1[n:], str2[n:], n)
        # returning the final strings with swapped characters 
        return (part1 + output[0], part2 + output[1])

#print(swap_chars("hello", "HELLO", 2))
#print(swap_chars("hello", "HELLO", 3))
#print(swap_chars("what a beautiful day", "sun is shining in new year's day", 4))


#function four - done 
def modify_order(some_list):
    if len(some_list) <= 2:
        return some_list
    #creating a new list to add values in the correct order 
    final_list = []
    # taking the first and last elements and adding to new list 
    final_list.append(some_list[0])
    final_list.append(some_list[-1])
    # using a recursive function starting from the second element so the process can repeat 
    return final_list + modify_order(some_list[1:-1])
    
#print(modify_order([1,2,3,4,5,6]))
#print(modify_order([7,18,'new', 4, 'hello']))
#print(modify_order([23,74,5,17,2,0,100,36,7]))
#print(modify_order([]))




#function 5 - done 
def subtract_inc(num1, num2, num3 = None):
	# checking to see if num3 has a value in first if - else statement
	#if no value given num3 not included 
    if num3 is None:
        if num1 >= num2:
            return 1 + subtract_inc(num1 - num2, num2 + 1)
        else:
            return 0 
    else:
    	#using recursive functions to subtract num2 and num3 from num1 while also increasing the value of num2 and num3 for every iteration
        if num1 > num2 and num1 < num3:
            return 1 + subtract_inc(num1 - num2, num2 + 1)
        elif num1 < num2 and num1 > num3:
            return 1 + subtract_inc(num1 - num3, num3 + 1)
        elif num1 < num2 and num1 < num3:
            return 0 
        else:
        	#using a counter in recursive function to see how many total times num2 and num3 can be subtracted from num1 
            output1 = 1 + subtract_inc(num1 - num2, num2 + 1)
            output2 = 1 + subtract_inc(num1 - num3, num3 + 1)
            #adding both counters together to get final result 
            return output1 + output2
    
            
#print(subtract_inc(10,2,5))
#print(subtract_inc(10, 2))
#print(subtract_inc(10,15,8))
#print(subtract_inc(100,50,10))

