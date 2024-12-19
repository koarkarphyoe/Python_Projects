intro_header_text="This program will introduce the details of fruits which are useful for health."
fruit_list_header_text="Fruit List"
fruit_list=["Apple","Orange",
            "Lemon","Mango",
            "Banana","Avocado",
            "Grape","Pear",
            "Papaya","Cucumber",
            "Durian","Pineapple",
            "Gourd","Cherry"]
details_fruit_list=[
    "Apples may have several benefits, including improved heart health and a lower risk of cancer and diabetes.",
    "The fiber in oranges can help blood sugar levels in check and reduce high cholesterol to prevent cardiovascular disease.",
    "Lemons are an excellent source of vitamin C and flavonoids, which are antioxidants. Antioxidants help remove free redicals that can damage cells from the body.",
    "Mangoes are also rich in vitamin C, which is important for forming bolld vessels and healthy collagen, as well as helping you heal.",
    "Bananas are a good source of several vitamins and minerals, especially potassium, vitamin B6 and vitamin C. Bananas area good source of potassium.A diet high in potassium can lower blood pressure in people with elevated levels and benefits heart health.",
    "One 7-ounce avocado provides 41percent of the daily value(DV) of folate, which helps produce healthy red blood cells.It also provides 14percent of the magnesium, which helps regulate bolld sugar levels and blood pressure.",
    "Grapes are rich in antioxidants which help protet the body's cells against oxidative stress, linked to cancer, heart disease and Alzheimer's disease.",
    "Pears have antioxidants, fiber, minerals and vitamins to benefit heart and gut health. They can also help lower your risk of diabetes.",
    "Papaya has many benefits, including protection against heart disease, reduced inflammation, aid in digestion, and boosting your immune system.",
    "Cucumber is a nutritious fruit with a high water content. Eating cucumber may help lower blood sugar, prevent constipation, and support weight loss.",
    "Eating durian may help support digestive health, heart health, weight management, and more.",
    "Pineappes are rich in flavonoids and phenolic acids, two antioxidants that protect your cells from free radicals that can cause chronic disease.",
    "As a rich source of antioxidants, flavonoids, and other polyphenol compounds, bitter gourd may help to reduce your risks for a number of health issues.",
    "Fresh cherries are full of minerals and other nutrients. Key among them is vitamin C."
]
print(intro_header_text)

quit_char='n'
while quit_char!='y':
    print(fruit_list_header_text)
    print("="*20)
    count=1
    for i in fruit_list:
        print(count,i)
        count=count+1
    print("="*20)

    input_char=input("Choose the number of fruit that you like to known about details:")
    if input_char.isnumeric():
        choose_num=int(input_char)
    # if choose_num in range(count):  
        if 0<choose_num<count: 
            print(fruit_list[choose_num-1])
            print(details_fruit_list[choose_num-1])
            quit_char=input("Do you like to quit? y/n:")
        else:
            print("Wrong input. The number should be between 1 and 14.")
            quit_char=input("Do you like to quit? y/n:")
        
    else:
        print("Wrong input. The number should be between 1 and 14.")
        quit_char=input("Do you like to quit? y/n:")
    
if quit_char=='y':
    for i in range(1,11):
        # print("="*(10-i),"Good Bye!","="*(10-i))
        # print(" "*(10-i),"*"*i,"Good Bye","*"*i," "*(10-i))
        if i<=5:
            print(" "*(11-i),"*"*i,"Good Bye","*"*i," "*(11-i))
        else:
            print(" "*i,"*"*(11-i),"Good Bye","*"*(11-i)," "*i)
