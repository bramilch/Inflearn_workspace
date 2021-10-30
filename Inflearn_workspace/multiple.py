print("구구단 몇단을 계산할까요?")
i = int(input())
print("구구단",i,"단을 계산합니다.")
for j in range(1,10):
    k = i * j
    print(i, "X", j, "=", k)

# print("구구단 몇단을 계산할까요?")
# user_input = input()
# print("구구단 " + user_input +"단을 계산합니다.")
# int_input = int(user_input)
# for i in range(1,10):
#     result = int_input * i
#     print(user_input, "X", i, "=", result)
