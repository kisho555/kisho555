import random

chars="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 ,<> : ? {} _ +"
while 1:  
 password_len = int(input("what length would you like your password to be :"))
 password_count = int (input("how many password would you like :"))
 for x in range (0,password_count):
     password ="_____"
     for x in range(0,password_len):
         password_char = random.choice(chars)
         password      = password + password_char
print("Here is your password:",password)
        
