
def first_unique_char(s: str) -> str:
   
    char_count = {}

   
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

 
    for char in s:
        if char_count[char] == 1:
            return char

    return "None"

s = "swiss"
print(first_unique_char(s))  