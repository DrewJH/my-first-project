import random

def generate_full_name(first_names, last_names):
	first_name = random.choice(first_names)
	last_name = random.choice(last_names)
	full_name = '{ln}, {fn}'.format(fn=first_name, ln=last_name)
	return full_name

def generate_age(age_start, age_stop):
	age = random.randint(age_start, age_stop)
	return age

def generate_birthdate(age):
	birthdate = age / 2
	birthdate = round(birthdate)
	return birthdate

def generate_person(first_names, last_names, age_start, age_stop):
	full_name = generate_full_name(first_names, last_names)
	age = generate_age(age_start, age_stop)
	birthdate = generate_birthdate(age)
	return {
		'full_name':full_name,
		'age':age,
		'birthdate':birthdate
	}

first_names = [
	'Bob',
	'George',
	'Ryan'
]

last_names = [
	'Dog',
	'Cat',
	'Parrott'
]

age_start = 30
age_stop = 55

person = generate_person(first_names, last_names, age_start, age_stop)
print (person)