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
reverse_array = []
x = len(user_array) - 1    
for i in range(len(user_array)):
    reverse_array.append(user_array[x])
    x = x - 1
print(reverse_array)