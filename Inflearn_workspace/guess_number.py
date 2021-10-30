import random
guess_number = random.randint(1,100)
print(guess_number)

user_input = int(input("숫자를 입력하세요."))
while(user_input != guess_number):
    if user_input > guess_number:
        print("숫자가 큽니다.")
    else: #if user_input < guess_number:
            print("숫자가 작습니다.")
    user_input = int(input("숫자를 입력하세요."))
print("맞았습니다.")
