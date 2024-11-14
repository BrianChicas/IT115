#
import json

#
data1 = {
    'name':'OJ Simpson',
    'age':30,
    'city': 'New York, NY',
    'interests':['Traveling', 'Football', 'Golf', 'Running', 'Videogames'],
    'is_student': False
    


}

data2 = {
    'name':'Brian Chicas',
    'age':22,
    'city': 'Seattle, WA',
    'interests':['Traveling', 'Soccer', 'Pokemon', 'Running', 'Videogames'],
    'is_student': True
    

}


with open('data1.json','w') as json_file:

    json.dump(data1,json_file,indent=4)
print("you have successfully written to data1.json")  

#######

with open ('data1.json', 'r') as json_file:

    loaded_data = json.load(json_file)

print("successfully able to read data1.json") 
print(loaded_data)
 

 #######


loaded_data['age'] = 11
loaded_data['interests'].append('RainbowSixSiege')

######## 

with open('data1.json','w') as json_file:

    json.dump(loaded_data,json_file,indent=4)
print("you have successfully re-written to data1.json")