def two_sum(number_array, target):
  ## 1. example input: [1,3,5,8,9]
  ## storage for indices
  result_indices = [];
  ## first cycle: going to retrieve the first number of the array
  ## second cycle: going to retrieve the following immediate number of the array
  for i in range(len(number_array)):
    current_number = number_array[i];
    ## next number
    for j in range(i+1, len(number_array)):
      next_number = number_array[j]
      ## now that we have two numbers, add them up
      if next_number + current_number == target:
        result_indices.append(i)
        result_indices.append(j)
  if not result_indices: 
    return "Not possible solution given the input array!"
  return result_indices;

print(two_sum([1,2,3,4,7], 7))