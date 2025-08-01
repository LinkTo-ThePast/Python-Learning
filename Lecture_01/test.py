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
  ## handling negative number case
  if (num < 0): 
    return False
  ## 1. store our original number
  x_original = num
  ## 2, intialize reverse_number
  x_reverse = 0
  while num > 0: 
    ## begin to remove characters right to left
    number_to_remove = num % 10;  
    ## add removed number into our reversed number and move it into the left ( x 10 );
    x_reverse = x_reverse * 10 + number_to_remove
    ## move to the next number to remove in our original number
    num = num // 10
  
  return x_reverse == x_original; 


##print(isPalindrome(1321));
print(isPalindromeWithoutString(121));
