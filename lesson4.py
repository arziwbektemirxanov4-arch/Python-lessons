
# Dictonaries - Dict - Key haam value den ibarat bolgan maglumat turleri

person = {
    "name" : 'John' , 
    "age" : 30 ,
    "city" : 'New York',
    "Speaks" : ['English', 'Spanish']
}
print(person)       # Output: {'name': 'John', 'age': 30, 'city': 'New York'}


# Dict Methods - Dict metodlari

#key() - Keylerin shig`aradi tek`
print(person.keys())        # Output: dict_keys(['name', 'age', 'city', 'Speaks'])

#value()  - Valuelerin shigaradi tek`
print(person.values())      # Output: dict_values(['John', 30, 'New York', ['English', 'Spanish']])

# get() - Key boyunsha valueni shigaradi
print(person.get("name"))   # Output: John


# items() - Key va value jupin shigaradi
print(person.items())       # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York'), ('Speaks', ['English', 'Spanish'])])

# update() - Dict ozgertiw
person.update({"age": 31})
print(person)               # Output: {'name': 'John', 'age': 31,

# copy() - Dict ni kopiyalaw
person_copy = person.copy()
print(person_copy)          # Output: {'name': 'John', 'age': 31

# Nested Dicts - Ishi ishli dictler
employee = {
    "name": "Jane",    
    "position": "Developer",
    "skills": {
        "programming": ["Python", "JavaScript"],
        "databases": ["MySQL", "MongoDB"]
    }
}
print(employee)            # Output: {'name': 'Alice', 'position': 'Developer',