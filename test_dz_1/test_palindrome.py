import test_palindrome
import unittest

def is_palindrome(s):
    return s == s[::-1]

class TestPalindrome(unittest.TestCase):

    

if __name__ == '__main__':
    test_palindrome.main()
