# STRING FUNCTIONS 


# Some of the commonly used functions to perform operations on or manipulate strings are as follows. Let us assume there is a string ‘str’ as follows: 

str = "Anees Ul Rehman"

# Now when operated on this string ‘str’, these functions do the following: 

# 1. len () function – This function returns the length of the strings. 
str="Anees Ul Rehman"
print(len(str))        #output: 15

# 2. String.endswith("man") – This function_ tells whether the variable string ends with the string "man" or not. If string is "Anees Ul Rehman", it returns true for "man" since Harry ends with man.

str="Anees Ul Rehman"
print(str.endswith("man"))  # Output: True

# 3. string.count("s") – counts the total number of occurrences of any character. 

str="Anees Ul Rehman"
count= str.count("e") 
print(count)  # Output: 3   bcuz this wil count how many 'e' in the "Anees Ul Rehman"

# 4. the first character of a given string. 
str="anees ul rehman"
capitalized_string=str.capitalize()
print(capitalized_string)    #output: "Anees ul rehman"
 
# 5. string.find(word) – This function friends a word and returns the index of first occurrence of that word in the string. 
str= "Anees Ul Rehman"
index= str.find("m")
print(index)   # Output 12 Bcuz m is 12 letter in "Anees Ul Rehman"

# 6. string.replace (old word, new word ) – This function replace the old word with new word in the entire string.
str= "Anees Ul Rehman"
replaced_string=str.replace("s","k")
print(replaced_string)


# some practice are here examples 

name= "Anees Ul Rehman Nohrio"
print(name)
print(len(name))
print(name.endswith("rry"))
print(name.startswith("An"))
# print(name.capitalize())
# print(name.startwith()) 

# name.find, this function the occurance that word in the sentence
a=name.find("Ul")
print(a)

# name.replace, This function change the old word to new word
# 1. i.e
replace=name.replace("e","b")
print(replace)

# 2. i.e
replace1=name.replace("U","L")
print(replace1)


n="Anees Ul Rehman is very intelligent student."
replace_n=n.replace("intelligent","weak")
print(replace_n)