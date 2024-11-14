#
import json

# Define data1 dictionary with information about a person
data1 = {
    'name':'OJ Simpson',
    'age':30,
    'city': 'New York, NY',
    'interests':['Traveling', 'Football', 'Golf', 'Running', 'Videogames'],
    'is_student': False
    


}
# Define data2 dictionary with information about another person
data2 = {
    'name':'Brian Chicas',
    'age':22,
    'city': 'Seattle, WA',
    'interests':['Traveling', 'Soccer', 'Pokemon', 'Running', 'Videogames'],
    'is_student': True
    

}

# Write data1 to a JSON file named 'data1.json'
with open('data1.json','w') as json_file:
# Save data1 with indentation for readability
    json.dump(data1,json_file,indent=4)
print("you have successfully written to data1.json")  


# Read data back from 'data1.json' into the variable loaded_data
with open ('data1.json', 'r') as json_file:
 # Load JSON data from the file
    loaded_data = json.load(json_file)

# Print the loaded data to verify contents
print("successfully able to read data1.json") 
print(loaded_data)
 



# Modify the loaded data
loaded_data['age'] = 22
loaded_data['interests'].append('RainbowSixSiege')


# Write the modified data back to 'data1.json', overwriting the original contents
with open('data1.json','w') as json_file:

# Save modified data with indentation
    json.dump(loaded_data,json_file,indent=4)

print("you have successfully re-written to data1.json")