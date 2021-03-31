import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier 
phone_number1 = phonenumbers.parse("+421915868073")
print(phone_number1)
print(geocoder.description_for_number(phone_number1,'sk'))
print(carrier.name_for_number(phone_number1,'sk')) 
phone_number2 = phonenumbers.parse("+421915868073")
print(geocoder.description_for_number(phone_number2,'sk'))
