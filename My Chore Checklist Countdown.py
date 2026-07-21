total = 4
done = 0
chore = 1

print("You have", total, "chores today!\n")

while chore <= total:
    if chore == 1:
        task = "Make your bed🛏️"
    elif chore == 2:
        task = "Feed the cat🐈"
    elif chore == 3:
        task = "Water the plants🪴"
    else:
        task = "Wash the dishes🍽️"

    answer = input("Did you finish: " + task + "? (yes/no):")

    if answer == "yes":
        done += 1
        chore += 1
        print("Good job!")
    else:
        print("Please finish it first!")

    print("Remaining:", total - done)
    print()

print("===== ALL CHORES COMPLETE! =====")

count = 0
while True:
    print("This loop could run forever!")
    count += 1
    if count == 3:
        print("Stopped using break.")
        break
    
print("\n===== SUMMARY =====")
print("Assigned:", total)
print("Completed:", done)
print("Remaining:", total - done)
