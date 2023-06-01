#age = 18
#print(age)

#lunch = 20
#dinner = 25
#week_spend = (lunch + dinner)*7
#print(week_spend)

#monthly = 2000
#dayly = monthly // 30
#dayly - round(monthly / 30)
#print(dayly)

#print(type("hello"))
#print("""
#1
#2
#3
#""")

#username = input("please enter your name:")
#date_of_birth = input("please enter your DOB:")#enter user name first, then the next question will be pop up
#print(username)
#print(date_of_birth)


import datetime
recipient_name = input("Enter the recipient's name: ")
year_of_birth = input("Enter the year of birth: ")
personalized_message = input("Enter a personalized message: ")
sender_name = input("Enter the sender's name: ")
you_are = 2023 - int(year_of_birth)

current_year = datetime.date.today().year
age = current_year - int(year_of_birth)

message = f"Dear {recipient_name},\n\n"
message += f"Here's a personalized message just for you:\n\n{personalized_message}\n\n"
message += f"All the best,\n{sender_name}"
message += f",your age is:\n{you_are}"

print("\n" + message)

# second try
# reciver_name = input("enter your name")
# msg = input("enter your DOB")
# sender_name = 2023 - int(msg)
# print(sender_name)
#print(reciver_name + "you born in" + msg + "your age is" + str(sender_name) + "years old")
