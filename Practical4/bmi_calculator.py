# BEGIN
#    PRINT "Please, give me your weight(kg) and height(m): "
#    READ input_string
#    SPLIT input_string BY "," INTO weight_string AND height_string

#    SET weight TO FLOAT(weight_string)
#    SET height TO FLOAT(height_string)

#    SET bmi TO weight / (height ^ 2)

#    IF bmi > 30 THEN
#        PRINT "Sorry, you are obese"
#    ELSE IF bmi < 18.5 THEN
#        PRINT "You are underweight"
#    ELSE
#        PRINT "You are normal weight"

x=input("Please, give me your weight(kg) and height(m),please separate them use comma: ").split(",")
weight=float(x[0])
height=float(x[1])
bmi=weight/height**2
if bmi>30:
    print(f"Your BMI is {bmi}, your are obese,sorry :(")
elif bmi<18.5:
    print(f"Your BMI is {bmi},you are underweight,sorry :(")
else:
    print(f"Your BMI is {bmi},You are normal weight :)")