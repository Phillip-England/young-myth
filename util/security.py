import bcrypt
import random
import string

def hash_value(some_string: str):
	salt = bcrypt.gensalt()
	hashed_value = bcrypt.hashpw(some_string.encode('utf-8'), salt)
	return hashed_value.decode('utf-8')

def check_hash(value: str, hashed_value: str):
    return bcrypt.checkpw(value.encode('utf-8'), hashed_value.encode('utf-8'))

def get_random_characters(some_number: int):
    characters = string.ascii_letters + string.digits  # You can include additional characters if needed
    random_string = ''.join(random.choices(characters, k=some_number))
    return random_string