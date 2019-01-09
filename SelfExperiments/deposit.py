firstPayment = 5000
additionalPayment = 5000
percents = 0.18
periodInMoth = 8 * 12
finalSum = 0

for i in range(periodInMoth):
    finalSum += round(additionalPayment + (finalSum * percents) / 12, 2)
    if i % 12 == 0:
        print("=============", round(i / 12, 0), "YEAR PASSED ==============")
    print("For this moth you'll get -", finalSum)
    print("Monthly percents =", finalSum * percents)
