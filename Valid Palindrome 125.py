
def isPalindrome(s):
    """
     :type s: str
        :rtype: bool
        """

    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    if cleaned == cleaned[::-1]:
        return True 
    else:
        return False

string ="A man, a plan, a canal: Panama"
print(isPalindrome(string))