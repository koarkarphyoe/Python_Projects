from datetime import datetime
import random

date_format_one="YYYY-MM-DD"
date_format_two="MM/DD/YYYY"
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
to_test_another=True
##choice date format
def date_format_check():
    while True:
        print("Date format options :"+"1."+date_format_one+","+"2."+date_format_two)
        choose_num=input("Choose a date format: ")
        if choose_num.isdigit():
            choose_num=int(choose_num)
            if(choose_num==1):
                user_input_date_validation(choose_num,random_date=None)
                return True
            elif(choose_num==2):
                user_input_date_validation(choose_num,random_date=None)
                return True
            else:
                date_format_check()
                return False
        else:
            print("Sorry => Please type numbers 1 or 2")
            
##check user input date is valid or not
def user_input_date_validation(choose_num,random_date):

    typed_format=True
    has_random_date=True
    while typed_format==True:
        user_typed_date=""
        if random_date==None:
            user_typed_date=input("Enter a date: ")
            has_random_date=False
        else:
            user_typed_date=random_date
        month=""
        day=""
        end_of_month=""
        next_year=""
        next_year_date_month=""
        if user_typed_date.__contains__("-") and choose_num==1:
            date_string=user_typed_date.split("-")
            date_format_one_list=date_format_one.split("-")
            date_format=dict(zip(date_format_one_list,date_string))
            month=int(date_format["MM"])
            day=int(date_format["DD"])
            next_year=int(date_format["YYYY"])+1
            next_year_date_month=str(next_year)+"-"+str(month)+"-"+str(day)
            random_date=None
            if 1<=month<12:
                end_of_month=days_in_month[month-1]
                if day>end_of_month:
                    if has_random_date==True:
                        typed_format=False
                        
                    print("Day is out of range.")
                    print("The date "+user_typed_date+" is not a valid date")
                else:
                    print("The weekday of "+user_typed_date+" is " +day_name(user_typed_date,"%Y-%m-%d"))
                    print("The date of a year after "+user_typed_date+" is "+next_year_date_month+"."+"It weekday is "+day_name(next_year_date_month,"%Y-%m-%d"))
                    typed_format=False
            else:
                if has_random_date==True:
                    typed_format=False
                    
                print("Month is out of range.")
                print("The date "+user_typed_date+" is not a valid date")
        elif user_typed_date.__contains__("/") and choose_num==2:
            date_string=user_typed_date.split("/")
            date_format_two_list=date_format_two.split("/")
            date_format=dict(zip(date_format_two_list,date_string))
            month=int(date_format["MM"])
            day=int(date_format["DD"])
            next_year=int(date_format["YYYY"])+1
            next_year_date_month=str(next_year)+"/"+str(month)+"/"+str(day)
            random_date=None
            if 1<=month<12:
                end_of_month=days_in_month[month-1]
                if day>end_of_month:
                    if has_random_date==True:
                        typed_format=False
                    
                    print("Day is out of range")
                    print("The date "+user_typed_date+" is not a valid date")
                else:
                    print("The weekday of "+user_typed_date+" is " +day_name(user_typed_date,"%m/%d/%Y"))
                    print("The date of a year after "+user_typed_date+" is "+next_year_date_month+"."+"It weekday is "+day_name(next_year_date_month,"%Y/%m/%d"))
                    typed_format=False
            else:
                if has_random_date==True:
                    typed_format=False
            
                print("Month is out of range.")
                print("The date "+user_typed_date+" is not a valid date")
        else:
            if choose_num==1:
                print("Error : "+str(choose_num)+" is not matched with -")
                typed_format=False
                if has_random_date==True:
                    print("The date format YYYY-MM-DD is not consistent with the date "+user_typed_date)
                else:
                    return None
            elif choose_num==2:
                print("Error : "+str(choose_num)+" is not matched with /")
                typed_format=False
                if has_random_date==True:
                    print("The date format MM/DD/YYY is not consistent with the date "+user_typed_date)
                else:
                    return None
        
##check weekday
def day_name(date_string,date_format):
    try:
        day_string=datetime.strptime(date_string,str(date_format))
        return day_string.strftime("%A")
    except ValueError as e:
        print("Error :"+str(e))
        return None
    
##random date
def random_auto_testing():
    choose_format=""
    choose_date_list=[]
    print("The random auto-testing is starting..... ")
    
    decoration_spacing()
        
    for i in range(10):
        random_year=str(random.randint(2000,2020))
        random_month=str(random.randint(1,19))
        random_day=str(random.randint(1,49))
        random_choose=random.choices([1,2])
        random_choose_format_number=int(random_choose[0])
        if random_choose_format_number==1:
            choose_format="YYYY-MM-DD"
        elif random_choose_format_number==2:
            choose_format="MM/DD/YYYY"
        random_choose_date_one=str(random_year+"-"+random_month+"-"+random_day)
        random_choose_date_two=str(random_month+"/"+random_day+"/"+random_year)
        combined_date_format=random.choices([random_choose_date_one,random_choose_date_two])
        choose_date=str(combined_date_format[0])
        choose_date_list.append(choose_date)
        print("The date to test :"+choose_date+" with the format "+choose_format)
        user_input_date_validation(random_choose_format_number,choose_date)
        
        decoration_spacing()
       
    
def decoration_spacing():
    ##to get space between auto testing
        for i in range(2):
            print(" "*10)
            
while to_test_another==True:
    date_format_check()
    
    decoration_spacing()
    ask_to_user=input("Do you like to test another?(y/n)")
    decoration_spacing()
    
    if ask_to_user=="y":
        to_test_another=True
    elif ask_to_user=="n":
        to_test_another=False
        random_auto_testing()
    else:
        print("Please type (y or n).")