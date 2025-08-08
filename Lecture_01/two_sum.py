def two_sum(number_array, target):
  ## 1. example input: [2, 9, 7, 10]; target = 11;
  indeces = [];
  for i in range(len(number_array)):
    current_number = number_array[i];
    print(current_number);
    for j in range(i+1,len(number_array)):
      next_number = number_array[j]
      print(next_number);
      if (current_number + next_number == target):
        indeces.append(i);
        indeces.append(j);
        return indeces;
  if len(indeces) == 0:
    return "Not possible solution given the input array!"
  
 ## not optimum