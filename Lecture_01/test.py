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

number = "123";
for i in range(len(number) - 1, -1,-1):
  print(number[i]);

""" def isPalindrome(number) -> bool:
  ## 1. convert into a string
  parsed_str_number: str = str(number);
  ## 2. reverse the string and then compare with the original 
  reversed_string = "";
  for i in range(len(parsed_str_number), 0, -1):
    current_char = parsed_str_number[i];
    print(current_char);
    reversed_string++current_char;

  print(reversed_string);


print(isPalindrome(123));
 """