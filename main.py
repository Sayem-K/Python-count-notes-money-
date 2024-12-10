amount = int(input("Enter the amount: "))
note_100 = amount // 100
amount = amount % 100
note_50 = amount // 50
amount = amount % 50
note_10 = amount // 10



print("Note 100:", note_100)
print("Note 50:", note_50)
print("Note 10:", note_10)
