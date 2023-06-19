def palindrome(n):
     
    if str(n) == str(n)[::-1]:
        print(True) 
    else: 
        print(False)
   
palindrome('лепсвпел')
