import random
import json

def random_line(filename):
    with open(filename) as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def random_address(filename):
    with open(filename) as f:
        data = json.load(f)
        random_address = random.choice(data['addresses'])
        return random_address

def get_full_person():
    data = random_address('data/address.json') 
    data['firstName'] = random_line('data/first_name.txt')
    data['lastName'] = random_line('data/last_name.txt')
    return data
