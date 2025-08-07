def two_sum(number_array, target):
  ## 1. example input: [2, 9, 7, 10]; target = 11;
  indeces = [];
  for i in range(len(number_array) - 1):
    current_number = number_array[i];
    print(current_number);
    for j in range(len(number_array) - 1):
      next_number = number_array[j+1]
      print(next_number);
      if (current_number + next_number == target):
        indeces.append(i);
        indeces.append(j+1);
        return indeces;
  if len(indeces) == 0:
    return "Not possible solution given the input array!"
  


print(two_sum([3,2,4], 6));

