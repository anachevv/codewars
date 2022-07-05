from pywebio import start_server
from pywebio.input import input, FLOAT
from pywebio.output import put_text


def main():  # PyWebIO application function
    def bmi_calculator():
        height = input('Input your height (cm):', type=FLOAT, required=True, placeholder='Your height')
        weight = input('Input your weight (kg):', type=FLOAT, required=True, placeholder='Your weight')

        bmi = weight / (height / 100) ** 2

        top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                      (25, 'Normal'), (30, 'Overweight'),
                      (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

        for top, top_status in top_status:
            if bmi <= top:
                put_text(f'Your BMI = {bmi:.1f} --> Category: {top_status}')
                break

    if __name__ == '__main__':
        bmi_calculator()


start_server(main, port=8080, debug=True)
