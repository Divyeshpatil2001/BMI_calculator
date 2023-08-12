def BMI(weight,  height):
    bmi = weight / (height/100)**2
    return bmi

height = float(input("Enter your Body Height:"))
weight = float(input("Enter your Body Weight:"))

bmi = BMI(weight,height)
print("The BMI is", (bmi), "so ", end='')

if (bmi < 18.5):
    print("underweight")
  
elif ( bmi >= 18.5 and bmi < 24.9):
    print("Healthy")
  
elif ( bmi >= 24.9 and bmi < 30):
    print("overweight")
  
elif ( bmi >=30):
    print("Suffering from Obesity")