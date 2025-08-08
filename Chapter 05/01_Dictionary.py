# DICTIONARY & SETS
# Dictionary is a collection of keys-value pairs. 

a = { 
"key": "value", 
"harry": "code", 
"marks": "100", 
"list": [1, 2, 9] 
} 
print(a["key"])  # Output: "value" 
print(a["list"])  # Output: [1, 2, 9] 
print(a["harry"])
print(a["marks"])


marks={
    "Anees":100,
    "Yasir":90,
    "Nasir":80,
    "Khalil":70,
    "Ikhtiar":60,
    "Abdul Rehman":50,
}
print(type(marks),"\n",marks)
print(
"Khalil",marks["Khalil"],"\n",
"Yasir",marks["Yasir"],"\n",
"Nasir",marks["Nasir"],"\n",
"Anees",marks["Anees"],"\n",
"Abdul Rehman",marks["Abdul Rehman"],"\n",
"Ikhtiar",marks["Ikhtiar"],"\n",)

print(
    "Khalil", marks["Khalil"], 
    "\nYasir", marks["Yasir"], 
    "\nNasir", marks["Nasir"], 
    "\nAnees", marks["Anees"], 
    "\nAbdul Rehman", marks["Abdul Rehman"], 
    "\nIkhtiar", marks["Ikhtiar"]
)

my_dict = {
    "name": "Anees",
    "message": """Hello Anees,
This is a multi-line
message stored in a dictionary.
No need to type \\n manually."""
}

print(my_dict["message"])
