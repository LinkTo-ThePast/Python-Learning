""" Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string? """


def isPalindrome(number) -> bool:
  ## 1. convert into a string
  parsed_str_number: str = str(number);
  ## 2. reverse the string and then compare with the original 
  reversed_string = "";
  for i in range(len(parsed_str_number) - 1, -1, -1):
    current_char = parsed_str_number[i];
    reversed_string += current_char;
  ## 3. final comparison:
  if (reversed_string == parsed_str_number):
    return True;
  else:
    return False;

def isPalindromeWithoutString(num) -> bool:
  ## handling case of negative numbers
  ## -121 !== 121-
  if (num < 0): 
    return False;

  ## begin inversion process
  # 1. store our original number
  original_number = num;
  # 2. initialize a new number: the reverse
  reversed_number = 0; 
  # 3. loop while num > 0
  ## input example: 151 ---> (1 * 10) posicional + removed number
  while num  > 0:
    current_removed_number = num % 10;
    reversed_number = (reversed_number * 10) + current_removed_number;
    num = num // 10
  return original_number == reversed_number;

##print(isPalindrome(1321));
print(isPalindromeWithoutString(1551));
