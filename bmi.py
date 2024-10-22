def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi= weight/(height*height)
    print("BMI = " + str(bmi))
    if bmi<18.5:
        print("You are Under Weight")
    elif bmi>25.0:
        print("You are Over Weight")
    else:
        print("You are Normal Weight")

calculate_bmi(weight=57, height=1.73)
