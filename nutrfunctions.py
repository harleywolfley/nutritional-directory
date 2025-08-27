import math

# DEFINE SOME VARIABLES

totalbmi = 0
newweight = 0
newheight = 0
EER = 0

# CONVERSIONS

def kg(weight):
    return weight * 0.453592

def meters(height):
    return height * 0.0254

# BMI

def bmi(newheight, newweight):
    return newweight / (newheight * newheight)

def prebmi(prepregweight, newheight):
    return prepregweight / (newheight * newheight)

# WEIGHT GAIN AND LOSS

def weightmath(howmuch):
    return 3500 * howmuch / 7

def addedcal(EER, gainmuch):
    return EER + gainmuch

# CALORIE FUNCTIONS

def calInfantThree(newweight):
    return (89 * newweight - 100) + 175

def calInfantSix(newweight):
    return (89 * newweight - 100) + 56

def calInfantTwelve(newweight):
    return (89 * newweight - 100) + 22

def calInfantThirtyFive(newweight):
    return (89 * newweight - 100) + 20

def calBy(age, PA, newheight, newweight):
    return 88.5 - (61.9 * age) + PA * ((26.7 * newweight) + (903 * newheight)) + 20

def calBo(age, PA, newheight, newweight):
    return 88.5 - (61.9 * age) + PA * ((26.7 * newweight) + (903 * newheight)) + 25

def calGy(age, PA, newheight, newweight):
    return 135.3 - (30.8 * age) + PA * ((10.0 * newweight) + (934 * newheight)) + 20

def calGo(age, PA, newheight, newweight):
    return 135.3 - (30.8 * age) + PA * ((10.0 * newweight) + (934 * newheight)) + 25

def calM(age, PA, newheight, newweight):
    return 662 - (9.53 * age) + PA * ((15.91 * newweight) + (539.6 * newheight))

def calW(age, PA, newheight, newweight):
    return 354 - (6.91 * age) + PA * ((9.36 * newweight) + (726 * newheight))

def calPFirst(EER):
    return EER + 0

def calPSecond (EER):
    return EER + 340

def calPThird (EER):
    return EER + 452

def calLactationSix(EER):
    return EER + 500 -170

def calLactationTwelve(EER):
    return EER + 400 - 0

# CARB AND FATS FUNCTIONs

def totalcarblow(finishcal):
    return finishcal * .45 / 4

def totalcarbhigh(finishcal):
    return finishcal * .65 / 4

def totalfatlow(finishcal):
    return finishcal * .20 / 9

def totalfathigh(finishcal):
    return finishcal * .35 / 9

def totalsatfat(finishcal):
    return finishcal * .10 / 9

# END FUNCTIONS

age = int(input(f"What is your age? \n"))
height = float(input(f"What is your height in inches? \n"))
weight = int(input(f"What is your weight in pounds? (Round to the nearest whole pound) \n"))
gender = input(f"Are you male (m) or female (f)? \n")
gender = gender.lower()
print("Physical Activity Definitions:\n" \
"Sedentary: Typical daily living activities (e.g. household tasks, walking to the bus)\n" \
"Low Active: Typical daily living activities PLUS 30-60 minutes of daily moderate activity (ex. walking at 5-7 km/h)\n" \
"Active: Typical daily living activities PLUS at least 60 minutes of daily moderate activity\n" \
"Very Active: Typical daily living activities PLUS at least 60 minutes of daily moderate activity PLUS an additional 60 minutes of vigorous activity or 120 minutes of moderate activity\n")
PA = input(f"What is your physical activity level? \n")
PA = PA.lower()

if gender == "m":
    newweight = kg(weight)
    newheight = meters(height)
    totalbmi = bmi(newheight, newweight)
    if PA == "sedentary":
        if age <= 18:
            PA = 1.00
        elif age >= 19:
            PA = 1.00
        else:
            print("Try again.")
    elif PA == "low active":
        if age <= 18:
            PA = 1.13
        elif age >= 19:
            PA = 1.11
        else:
            print("Try again.")
    elif PA == "active":
        if age <= 18:
            PA = 1.26
        elif age >= 19:
            PA = 1.25
        else:
            print("Try again.")
    elif PA == "very active":
        if age <= 18:
            PA = 1.42
        elif age >= 19:
            PA = 1.48
        else:
            print("Try again.")
    else:
        print("Try again.")
    EER = calM(age, PA, newheight, newweight)
    pregnancy = "neither"
    print()
elif gender == "f":
    newweight = kg(weight)
    newheight = meters(height)
    totalbmi = bmi(newheight, newweight)
    if PA == "sedentary":
        if age <= 18:
            PA = 1.00
        elif age >= 19:
            PA = 1.00
        else:
            print("Try again.")
    elif PA == "low active":
        if age <= 18:
            PA = 1.16
        elif age >= 19:
            PA = 1.12
        else:
            print("Try again.")
    elif PA == "active":
        if age <= 18:
            PA = 1.31
        elif age >= 19:
            PA = 1.27
        else:
            print("Try again.")
    elif PA == "very active":
        if age <= 18:
            PA = 1.56
        elif age >= 19:
            PA = 1.45
        else:
            print("Try again.")
    else:
        print("Try again.")
    EER = calW(age, PA, newheight, newweight)
    pregnancy = input(f"Are you pregnant, breastfeeding, or neither? \n")
    pregnancy = pregnancy.lower()
    if pregnancy == "pregnant":
        wks = int(input(f"How many full weeks are you in your pregnancy? \n"))
        prepregweight = float(input("What was your weight before pregnancy? \n"))
        prepregweight = kg(prepregweight)
        if wks <= 12:
            EER = calPFirst(EER)
        elif wks <= 27:
            EER = calPSecond(EER)
        elif wks <= 40:
            EER = calPThird(EER)
        else:
            print()
        print()
    elif pregnancy == "breastfeeding":
        wks = int(input(f"How many full months are you postpartum? \n"))
        if wks <= 6:
            EER = calLactationSix(EER)
        elif wks <= 12:
            EER = calLactationTwelve(EER)
        else:
            print("Postpartum tracks between 0-12 months. Try Again.")
    elif pregnancy == "neither":
        print()
    else:
        print("Please enter 'pregnant', 'breastfeeding', or 'neither'.")
else:
    print("Please enter a value 'm' or 'f' for gender.")

# WEIGHT GOALS

goal = input(f"Are you looking to gain, lose, or maintain weight? \n")
goal = goal.lower()
if goal == "gain":
    if pregnancy == "pregnant":
        howmuch = 1
        gainmuch = weightmath(howmuch)
        print()
    else:
        howmuch = int(input("How many pounds would you like to gain per week? \n"))
        gainmuch = weightmath(howmuch)
    if pregnancy == "pregnant":
        pregbmi = prebmi(prepregweight, newheight)
        if pregbmi <= 18.5:
            print(f"The total weight gained during pregnancy should be 28-40 pounds. \n")
            if wks <= 13:
                print("You should gain 2-4 pounds during the first trimester.")
            elif wks >= 14:
                print("You should gain at least 1 pound per week until birth. \n")
            else:
                print()
        elif pregbmi <= 24.9:
            print(f"The total weight gained during pregnancy should be 25-35 pounds. \n")
            if wks <= 13:
                print("You should gain 2-4 pounds during the first trimester.")
            elif wks >= 14:
                print("You should gain 1/2 - 1 pound per week until birth. \n")
            else:
                print()
        elif pregbmi <= 29.9:
            print(f"The total weight gained during pregnancy should be 15-25 pounds. \n")
            if wks <= 13:
                print("You should gain 2-4 pounds during the first trimester.")
            elif wks >= 14:
                print("You should gain 1/2 - 1 pound per week until birth. \n")
            else:
                print()
        elif pregbmi >= 30:
            print(f"The total weight gained during pregnancy should be 11-20 pounds. \n")
            if wks <= 13:
                print("You should gain 2-4 pounds during the first trimester.")
            elif wks >= 14:
                print("You should gain half a pound per week until birth. \n")
            else:
                print()
        else:
            print()
    else:
        print()
        print(f"Increase your calorie intake by {gainmuch:.0f} calories per day in addition to replacing the calories you burn with physical activity.")
    if howmuch >= 2.1:
        print("Gaining more than 2 pounds a week is typically discouraged.")
        print()
    else:
        print()
elif goal == "lose":
    if pregnancy == "pregnant":
        howmuch = 1
        gainmuch = weightmath(howmuch)
        print()
    elif pregnancy == "breastfeeding":
        howmuch = 1
        gainmuch = weightmath(howmuch)
        print()
    else:
        howmuch = float(input("How many pounds would you like to lose per week? \n"))
        gainmuch = weightmath(howmuch)
        print(f"Decrease your calorie intake by {gainmuch:.0f} calories per day through calories you burn with physical activity or reducing food intake.")
    if howmuch >= 2.1:
        print("Losing more than 2 pounds a week is typically discouraged.")
        print()
    else:
        print()
    if pregnancy == "pregnant":
        print("Weight loss is highly discouraged during pregnancy. It can cause improper development of the child and/or loss of nutrient levels in the mother. It is dangerous to both mother and child to lose weight. Results can be fatal.")
elif goal == "maintain":
    if pregnancy == "breastfeeding":
        howmuch = 0
        gainmuch = weightmath(howmuch)
        print()
    elif pregnancy == "breastfeeding":
        howmuch = 0
        gainmuch = weightmath(howmuch)
        print()
    else:
        howmuch = 0
        gainmuch = weightmath(howmuch)
        print()
    print("Continue recommendeded calorie intake. \n")
else:
    print("Try again.")

finishcal = addedcal(EER, gainmuch)

# TOTAL BMI

if totalbmi <= 18.49999:
    print(f"Your BMI is: {totalbmi:.0f}. You are Under Weight.\n")
elif totalbmi <= 24.99999:
    print(f"Your BMI is: {totalbmi:.0f}. You have a Healthy Weight.\n")
elif totalbmi <= 29.99999:
    print(f"Your BMI is: {totalbmi:.0f}. You are Overweight.\n")
elif totalbmi <= 39.99999:
    print(f"Your BMI is: {totalbmi:.0f}. You are Obese.")
elif totalbmi >= 40:
    print(f"Your BMI is: {totalbmi:.0f}. You are Extremely Obese.")

# RECOMMENDED CALORIES

print(f"Your EER (Estimated Energy Requirement) is {EER:.0f} Calories per day. \n")

# CARBS

lowcarbsneeded = totalcarblow(finishcal)
highcarbsneeded = totalcarbhigh(finishcal)
print(f"Total carbohydrates needed: {lowcarbsneeded:.0f} - {highcarbsneeded:.0f} grams, 45-65% of daily calories. \n")

# RECOMMENDED PROTEIN

proteinrecommendlow = EER * .10
proteinrecommendhigh = EER * .35
if pregnancy == "pregnant":
    proteinrecommendg = 1.1 * newweight
    print(f"Total protein needed: {proteinrecommendg:.0f} grams. ")
elif pregnancy == "breastfeeding":
    proteinrecommendg = 1.1 * newweight
    print(f"Total protein needed: {proteinrecommendg:.0f} grams. ")
elif pregnancy == "neither":
    proteinrecommendg = 0.8 * newweight
    print(f"Total protein needed: {proteinrecommendg:.0f} grams. ")
else:
    proteinrecommendg = 0.8 * newweight
    print(f"Total protein needed: {proteinrecommendg:.0f} grams. ")

print(f"Your protein intake should be 10-35% of your calories per day. Your recommended protein intake, under normal circumstances, is {proteinrecommendlow:.0f} - {proteinrecommendhigh:.0f} calories.")
print()

# FATS, SATURATED

lowfatsneeded = totalfatlow(finishcal)
highfatsneeded = totalfathigh(finishcal)
saturatedfat = totalsatfat(finishcal)
print(f"Total fats needed: {lowfatsneeded:.0f} - {highfatsneeded:.0f} grams, 20-35% of daily calories.")
print(f"Total saturated fats needed: {saturatedfat:.0f} grams, 10% of daily calories.")
