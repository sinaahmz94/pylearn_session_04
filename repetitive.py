user_array = []
print("computer will recieve the numbers until you type 00")
while True:
    user_num = int(input("please enter number: "))   
    if user_num != 00:    
        user_array.append(user_num)
        print(user_array)
    else:
        print(user_array)
        break
non_repetitive_array = []
for i in range(len(user_array)):
    if user_array[i] not in non_repetitive_array:
        non_repetitive_array.append(user_array[i])
print(non_repetitive_array)
