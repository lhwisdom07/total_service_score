dayScore = 0
numberOfDays = int(input("How many days of scores? "))
for daysLeft in range( 1, numberOfDays +1):
    dayScore = dayScore + int(input("Enter score for day" + str(daysLeft) + ':'))
print("The total score of the", str(numberOfDays), "days is", str(dayScore))