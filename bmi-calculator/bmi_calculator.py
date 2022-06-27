from pywebio.input import input, FLOAT
from pywebio.output import put_text


def bmi_calculator():

    # Taking user's height and weight.

    height = input('Input your height (cm):', type=FLOAT, required=True, placeholder='Your height')
    weight = input('Input your weight (kg):', type=FLOAT, required=True, placeholder='Your weight')

    # Calculating user's BMI

    bmi = weight / (height / 100) ** 2

    # BMI result column

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    # Printing user's BMI result and its certain category

    for top, top_status in top_status:
        if bmi <= top:
            put_text(f'Your BMI = {bmi:.1f} --> Category: {top_status}')
            break


# Running the script

if __name__ == '__main__':
    bmi_calculator()
