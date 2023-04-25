import qrcode

name = input("please enter your name: ")
phone_number = input("please enter your phone number")
img = qrcode.make(name|phone_number)
img.save("your_qrcode.png")