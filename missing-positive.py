array_of_numbers1 = [3,4,-1,1]
array_of_numbers2 = [2,1,0]

def first_missing_positive(numbers):
    
    minimum_number = numbers[0]
    maximum_number = numbers[0]
    output = 0
    
    for i in range(len(numbers)):
        
        # get the maximum number and the minimum number from the array
        if minimum_number > numbers[i]:
            minimum_number = numbers[i]
            
        if maximum_number < numbers[i]:
            maximum_number = numbers[i]
        
        # handle negative numbers
        if maximum_number <= 0:
            return "No positive numbers"
        
        if minimum_number <= 0:
            minimum_number = 1
            
    # iterating from the minimum adding 1 to find the missing number
    for j in range(minimum_number,maximum_number):
        found = False
        
        for k in range(len(numbers)):
                if numbers[k] == j:
                    found = True
                    break
                
        if not found:
            output = j
            return output
        
        if found and j == maximum_number-1:
            output = maximum_number + 1
            return output
        
    return output 

result = first_missing_positive(array_of_numbers1)
print("the output is: ", result)
            
            
            
                  
        
