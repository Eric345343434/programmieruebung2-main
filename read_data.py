import json
def get_person_data():
 
# Opening JSON file
 file = open("data/person_db.json")

# Loading the JSON File in a dictionary
 person_data = json.load(file)
 
 return person_data



def get_person_names():

 person_data = get_person_data()
 list_with_person_names = []
 for person in person_data:
  print(person["firstname"])
  list_with_person_names.append(person["lastname"]+ ", " +person["firstname"])
 return list_with_person_names

if __name__ == "__main__":
 person_names_list = get_person_names()
 print(person_names_list)
    
    
    
    
    

   