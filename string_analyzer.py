# Problem

# Create a program that accepts a sentence and analyzes it.

# Calculate:

# Total characters
# Total words
# Number of vowels
# Number of consonants
# Number of digits
# Number of spaces
# Number of special characters
# Most frequent character

# Ignore uppercase/lowercase differences when counting.
class String_analyzer:
    def __init__(self,data):
        self.data = data
    def total_charactor(self):
        print(f"Total Charactor :{len(self.data)}")
    def total_word(self):
        print(len(self.data.split()))
    def  vowel_counter(self):
        count = 0
        for i  in self.data.lower():
            if i  in "aeiou":
                count+=1
        print(f"Total Count : {count}")
    def consonant_values(self):
        count = 0
        for i in self.data.lower():
            if i in "aeiou":
                continue
            elif i.isalpha(): 
                count+=1
        print(f"Total consonant : {count}") 
    def digit_in(self):
        count = 0
        for i in self.data:
            if i.isdigit():
                count +=1
        print(f"Digits :{count}")
    def space_checker(self):
        count = 0
        for i in self.data:
            if i.isspace():
                count +=1
        print(f"Total Spaces : {count}")
    def speical_charactor(self):
        count = 0
        for i in self.data:
            if i  in "!@#$%^&*":
                count+=1
        print(f"Special_Charactor : {count}")
    def frequent_charactor(self):
        frequency = {}
        for i in self.data.lower():
            if i != " ":
               frequency[i] = frequency.get(i,0)+1
        print(frequency)
        
string_analyzer = String_analyzer("I am  name is  Adnan")
string_analyzer.consonant_values()
string_analyzer.digit_in()
string_analyzer.frequent_charactor()
string_analyzer.space_checker()
string_analyzer.total_charactor()
string_analyzer.vowel_counter()
string_analyzer.speical_charactor()