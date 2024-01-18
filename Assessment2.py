items = {
    '0': {'Name': 'Pepsi', 'price': 1 
    },
      '1': {'Name': 'Redbull', 'price': 4
    },
      '2': {'Name': 'Cola', 'price': 2
     },       
      '3': {'Name': 'Fanta', 'price': 2
     },       
      '4': {'Name': 'Sprite', 'price': 2
    },        
      '5': {'Name': 'Dew', 'price': 1.50
     },       
      '6': {'Name': 'Oman Chips', 'price': 3
     },       
      '7': {'Name': 'Amwaaj Chips', 'price': 3
    },        
      '8': {'Name': 'Twix', 'price': 3      
    },        
      '9': {'Name': 'KitKat', 'price': 3}
      
}
print("Welcome to the Vending Machine!")
print("Please select an item:")

for key, items in items.items():
    print(f"{key}. {items['Name']} - {items['price']} AED")

x=str(input('\nEnter The Item Number You Would Like To Buy:\n'))
if x == '0':
    print('You have chosen Pepsi!')
    y = float(input("Pay the amount:\n"))
    pepsi = 2
    if y > pepsi:
        print("Take your change with your selected item: ", y - pepsi)
    elif y < pepsi:
        print("no enough money")
        print("Amount refunded")
    elif y == pepsi:
        print("Here is your Pepsi")

elif x == '1':
    print('You have chosen RedBUll!')
    y = float(input("Pay the amount:\n"))
    Redbull = 4
    if y > Redbull:
        print("Take your change with your selected item: ", y - Redbull)
    elif y < Redbull:
        print("no enough money")
        print("Amount refunded")
    elif y == Redbull:
        print("Here is your Redbull")

elif x == '2':
    print('You have chosen Cola!')
    y = float(input("Pay the amount:\n"))
    Cola = 2
    if y > Cola:
        print("Take your change with your selected item: ", y - Cola)
    elif y < Cola:
        print("no enough money")
        print("Amount refunded")
    elif y == Cola:
        print("Here is your Cola ")

elif x == '3':
    print('You have chosen Fanta!')
    y = float(input("Pay the amount:\n"))
    Fanta = 2
    if y > Fanta:
        print("Take your change with your selected item: ", y - Fanta)
    elif y < Fanta:
        print("no enough money")
        print("Amount refunded")
    elif y == Fanta:
        print("Here is your Fanta")

elif x == '4':
    print('You have chosen Sprite!')
    y = float(input("Pay the amount:\n"))
    Sprite = 1
    if y > Sprite:
        print("Take your change with your selected item: ", y - Sprite)
    elif y < Sprite:
        print("no enough money")
        print("Amount refunded")
    elif y == Sprite:
        print("Here is your Sprite")

elif x == '5':
    print('You have chosen Dew!')
    y = float(input("Pay the amount:\n"))
    Dew = 1.50
    if y > Dew:
        print("Take your change with your selected item: ", y - Dew)
    elif y < Dew:
        print("no enough money")
        print("Amount refunded")
    elif y == Dew:
        print("Here is your Redbull")

elif x == '6':
    print('You have chosen Omaan Chips!')
    y = float(input("Pay the amount:\n"))
    OmanChips = 3
    if y > OmanChips:
        print("Take your change with your selected item: ", y - OmanChips)
    elif y < OmanChips:
        print("no enough money")
        print("Amount refunded")
    elif y == OmanChips:
        print("Here is your Oman Chips")

elif x == '7':
    print('You have chosen Amwaaj Chips!')
    y = float(input("Pay the amount:\n"))
    AmwaajChips = 3
    if y > AmwaajChips:
        print("Take your change with your selected item: ", y - AmwaajChips)
    elif y < AmwaajChips:
        print("no enough money")
        print("Amount refunded")
    elif y == AmwaajChips:
        print("Here is your Amwaaj Chips")

elif x == '8':
    print('You have chosen Twix!')
    y = float(input("Pay the amount:\n"))
    Twix = 3
    if y > Twix:
        print("Take your change with your select0ed item: ", y - Twix)
    elif y < Twix:
        print("no enough money")
        print("Amount refunded")
    elif y == Twix:
        print("Here is your Twix")

elif x == '9':
    print('You have chosen KitKat!')
    y = float(input("Pay the amount:\n"))
    KitKat = 1
    if y > KitKat:
        KitKat("Take your change with your selected item: ", y - KitKat)
    elif y < KitKat:
        print("no enough money")
        print("Amount refunded")
    elif y == KitKat:
        print("Here is your KitKat")
