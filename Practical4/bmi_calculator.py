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

x=input("Please, give me your weight(kg) and height(m): ").split(",")
weight=float(x[0])
height=float(x[1])
bmi=weight/height**2
if bmi>30:
    print("Sorry,you are obese")
elif bmi<18.5:
    print("you are underweight")
else:
    print("You are normal weight")