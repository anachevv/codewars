# THIS IS A SIMPLE hide_credit_card_number CODE! IT IS NOT INTENDED FOR SERIOUS USE!






# def hide():
#     card_number = input("Please input your credit card number:\n")
#     card_number_length = len(card_number)
#     hidden_number = card_number.replace(str(card_number[0:-4]), (card_number_length - 4) * "*")
#
#     return print(hidden_number)
#
#
# hide()

card_number = input("Please insert your credit card number:\n")
card_number_length = len(card_number)

while card_number_length != 16:
    another_card_number = input("Error! Please insert a valid card number!\n")

    if card_number_length == 16:
        hidden_number = card_number.replace(str(card_number[0:-4]), (card_number_length - 4) * "*")
        print(hidden_number)
        break

    if len(another_card_number) == 16:
        hidden_number = another_card_number.replace(str(another_card_number[0:-4]),
                                                    (len(another_card_number) - 4) * "*")
        print(hidden_number)
        break
    elif len(another_card_number) < 16 or len(another_card_number) > 16:
        another_card_number = input("Error! Please insert a valid card number!\n")

    card_number = input("Error! Please insert a valid card number!\n")

# 16 digits only!
