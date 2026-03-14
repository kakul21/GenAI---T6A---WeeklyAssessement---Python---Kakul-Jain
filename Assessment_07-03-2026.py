# Problem 1
'''Password Strength Validator
Problem Description
A website checks the strength of passwords. A password is considered strong if it satisfies the following rules:

Length must be at least 8 characters

Must contain at least one uppercase letter

Must contain at least one digit

Must contain at least one special character (@, #, $)

Given a list of passwords, return a list containing only strong passwords.'''

#solution 1
class Solution:
    def strong_passwords(self, passwords):
        strong = []
        special_chars = "@#$"
        
        for password in passwords:
            
            has_upper = False
            has_digit = False
            has_special = False
            
            if len(password) >= 8:
                
                for ch in password:
                    
                    if ch.isupper():
                        has_upper = True
                    
                    elif ch.isdigit():
                        has_digit = True
                    
                    elif ch in special_chars:
                        has_special = True
                
                if has_upper and has_digit and has_special:
                    strong.append(password)
       
        return strong

# Problem 2
'''Password Strength Validator
Problem Description
A website checks the strength of passwords. A password is considered strong if it satisfies the following rules:

Length must be at least 8 characters

Must contain at least one uppercase letter

Must contain at least one digit

Must contain at least one special character (@, #, $)

Given a list of passwords, return a list containing only strong passwords.'''

#solution 2
class Solution:
    def low_stock_products(self, inventory):
        result = []
        
        for product, quantity in inventory.items():
            if quantity < 10:
                result.append(product)
        
        return result

# Problem 3
'''Consecutive Duplicate Word Detector
Problem Description
A text processing tool analyzes sentences to find consecutive duplicate words.

If the same word appears next to each other, ignoring case differences, it should be recorded.

Return a list of such duplicate words.

Input
A sentence string.

Output
List of duplicate consecutive words.'''

#solution 3
class Solution:
    def find_duplicate_words(self, sentence):
        words = sentence.lower().split()
        duplicates = []
        
        for i in range(len(words) - 1):
            if words[i] == words[i + 1]:
                duplicates.append(words[i])
       
        return duplicates

# Problem 4
'''Unique Product Purchase Analyzer
Problem Description
An e-commerce company records the products purchased by customers during a sale. However, some products appear multiple times in the purchase list because multiple customers bought them.

The company wants to generate a list of unique products that were purchased only once during the sale.

You are given a list of product names representing purchases. Your task is to return a list containing products that appear exactly once in the list.

Input
A list of product names.

Example
["Laptop","Mouse","Keyboard","Mouse","Monitor","Keyboard","Tablet"]
Output
["Laptop","Monitor","Tablet"]'''

#solution 4
class Solution:
    def unique_products(self, products):
        result = []
        for product in products:
            if products.count(product)==1:
                result.append(product)
         
        return result


