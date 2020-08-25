import re


def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b') 
	# creating the regex pattern to match with

	# checking if there is a match.
	match = phone_regex.search(input)
	if match:
		return match.group()
	return None

# Returns all instances of phone number pattern in a list
def extract_all_phones(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)


def is_valid_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.fullmatch(input)
	if match:
		return True
	return False

# Calling our functions a bunch of times...

print(extract_phone("my number is 432 567-8976"))
print(extract_phone("my number is 432 567-897622"))
print(extract_phone("432 567-8976 asdjhasd "))
print(extract_phone("432 567-8976"))

print(extract_all_phones("my number is 432 567-8976 or call me at 345 666-7899"))
print(extract_all_phones("my number is 432 56"))

print(is_valid_phone("432 567-8976"))
print(is_valid_phone("432 567-8976 ads"))
print(is_valid_phone("asd 432 567-8976 d"))



