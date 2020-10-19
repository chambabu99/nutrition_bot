import random
from datetime import datetime
def greet_and_intro():
    responses=[
        "Hi There! I am nutrition details describing bot.I can help you to get some information about the vitamins in various fuits.May i know your name please ?",
        "Wounderful, It is so nice to be in touch with you.I am a nutrition details describing bot."
    ]
    print(random.choice(responses))

def get_date_time():
    current_time = datetime.now()
    timeofday_greeting = "Good Morning"
    if current_time.hour > 12 and current_time.hour <= 17:
        timeofday_greeting = "Good Afternoon"
    elif current_time.hour > 17 and current_time.hour <= 22:
        timeofday_greeting = "Good Evening"
    elif current_time.hour >= 22:
        timeofday_greeting = "Hi!!,Thats late!!"
    return timeofday_greeting 

def welcome(name):
    message=[
        "Nice to meet you ",
        "Very good to be in touch with you "
    ]
    print(f"{get_date_time()} {random.choice(message)}{name}")

def bot_details():
    print("1.calculator")
    print("2.nutrition ")
    try:
        return input("Enter the name to get that bot details :")
    except:
        print("Not able to provide information.")
        return 0

def calculator_details():
    print("1.Calculate an expression")
    print("2.Get current time")
    print("3.End this chat")
    print("-----------------------")
    try:
        return int(input("Enter your choice[1-3] : "))
    except:
        print("Only enter choice from 1 to 3")
        return 0

def evaluate_exp():
    expr=input("Enter an expression")
    try:
        print("Result = ",eval(expr))
    except Exception as e:
        print(str(e))

def nutrition_list():
    print("This is the list vitamins present in different fruits:")
    print("1.Pineapple")
    print("2.Oraange")
    print("3.Apple")
    print("4.Banana")
    print("5.Blackberries")
    print("6.To stop conversation.")
    print("-----------------------")
    try:
        return int(input("Enter your choice[1-6] : "))
    except:
        print("Only enter choice from 1 to 6 ")
        return 0
def bot():
    greet_and_intro()
    name = input("Your Name : ")
    welcome(name)
    bot_info = bot_details()
    if(bot_info == "calculator"):
        choice=calculator_details()
        while choice != 3:
            if choice ==1:
                evaluate_exp()
                print("-----------------------")
            elif choice ==2:
                print(str(datetime.now()))
            else:
                print("I don't understand that")
            choice=calculator_details()
    elif(bot_info == "nutrition" ):
        print("Enter the number of the fruit .To get information about the vitamins present in it")
        choice=nutrition_list()
        while choice != 6:
            if choice ==1:
                print("The vitamin present in pineapple are")
                print("vitamin A, vitamin B1, vitamin B2, vitamins B6, vitamin C, Folate(folic acid)")
                print("----------------------------------------------------------")
            elif choice ==2:
                print("The vitamins present in orange are:")
                print("vitamin A, vitamin B1,vitamin B2,vitamin B6,vitamin C, Folate(folic acid)")
                print("------------------------------------------------------------")
            elif choice ==3:
                print("The vitamin present in Apple are")
                print("vitamin A, vitamin B1, vitamin B2, vitamins B6, vitamin C, Folate(folic acid)")
                print("------------------------------------------------------------")
            elif choice ==4:
                print("The vitamin present in Banana are")
                print("vitamin A, vitamin B1, vitamin B2, vitamins B6, vitamin C, Folate(folic acid)")
                print("-----------------------------------------------------------")
            elif choice ==5:
                print("The vitamin present in Blackberries are")
                print("vitamin A, vitamin B1, vitamin B2, vitamins B6, vitamin C, Folate(folic acid)")
                print("------------------------------------------------------------")
            else:
                print("I don't understand that")
                print("-----------------------")
            choice=nutrition_list()
    else:
        print("Sorry unable aceppt your request.")

bot()