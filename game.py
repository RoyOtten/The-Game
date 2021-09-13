print ("welcome to Ragnarok")
print ("this game is about a young hero against a god oin the norse mythology")
name = input ("tell me your name")
print ("you wake up with a strange feeling") 
print ("hello " +  name + " you're finally awake")  
print ("the village up above has been attacked overnight, you have to check on them") 
print ("you feel very anxious aboout the situation")
print ("you have the option to rest a little longer and go to the village feeling well and rested, or you go now with the anxious and tired feeling") 
stage1 = input ("do you wanna rest longer?")
if stage1 == ("yes"): 
    print ("you wake up again feeling refreshed and ready to go to the village") 
    stagevraag1 = input ("head to the village?")
    if stagevraag1 == ("yes"):
        print ("you head to the village")
        print ("along the way you find a stressed man with a broken carriage with alot of food") 
        stagevraag2 = input ("will you help the man?")
        if stagevraag2 == ("yes"):
            print ("you help the man with his carriage, apparently the man had to go to the village with this food and offers you a ride to the village") 
        elif stagevraag2 == ("no"):
            print ("you walk past the helpless man without showing any mercy, you cruel man") 
    if stagevraag1 == ("no"):
        print ("you rest a little longer and then force yourself to the road of the village")
        print ("along the way you find a stressed man with a broken carriage") 
        stagevraag3 = input ("will you help the man") 
        if stagevraag3 == ("yes"):
            print ("you are too tired to help the man and walk past the man feeling tired") 
        elif stagevraag3 == ("no"):
            print ("you walk past the helpless man without any mercy, you cruel man") 
if stage1 == ("no"):
    print ("bad choice")
    stagevraag1 = input ("head to the village?")
    if stagevraag1 == ("yes"):
        print ("you head to the village")
        print ("along the way you find a stressed man with a broken carriage with alot of food") 
        stagevraag2 = input ("will you help the man?")
        if stagevraag2 == ("yes"):
            print ("you are too tired to help the man") 
        elif stagevraag2 == ("no"):
            print ("you walk past the helpless man without showing any mercy, you cruel man") 
    if stagevraag1 == ("no"):
        print ("you rest a little longer and then force yourself to the road of the village")
        print ("along the way you find a stressed man with a broken carriage") 
        stagevraag3 = input ("will you help the man") 
        if stagevraag3 == ("yes"):
            print ("you are too tired to help the man and walk past the man feeling tired") 
        elif stagevraag3 == ("no"):
            print ("you walk past the helpless man without any mercy, you cruel man")
print ("you arrive at the village and you can already see the village took alot of damage") 
if stage1 == ("yes") and stagevraag1 == ("yes") and stagevraag2 == ("yes"):
    print ("you arrive at the village with the man and the 2 of you help any people in need with the food from the carriage, you win")
else:
    print ("the people are in need of food and water, you feel too tired to be able to help them, you lose") 


    

    




