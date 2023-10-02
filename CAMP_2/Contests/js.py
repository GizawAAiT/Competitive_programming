# importing json module
import json
# input dictionary
dict = {
   "id": ("1", "2", "3"),
   "languages": ("python", "java", "c++"),
   "authors": ("abc", "xyz", "pqr")
}  
# converting dictionary of tuples into json
result = json.dumps(dict, indent=0)
# printing the resultant json
print(result)