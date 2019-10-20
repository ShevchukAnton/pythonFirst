def is_number(inp):
    while True:
        try:
            inp = int(inp)
        except ValueError:
            print("It's not a fucking integer.")
            continue
        else:
            return inp


firstPayment = is_number(input('Enter first payment:\n'))
additionalPayment = is_number(input('Enter monthly payment:\n'))
annualPercents = is_number(input('What is the annual percents:\n'))
monthlyPercents = (annualPercents / 100) / 12
taxes = 0.2
years = is_number(input('For how many years you want to keep deposit:\n'))
periodInMonth = 12 * years
finalSum = (firstPayment * monthlyPercents) - ((firstPayment * monthlyPercents) * taxes)

for i in range(periodInMonth):
    finalSum += additionalPayment + (finalSum * monthlyPercents)
    if i % 12 == 0 and i > 0:
        print("=============", round(i / 12, 0), "YEAR(S) PASSED ==============")
    print("For this month you'll get -", round(finalSum, 2))
    print("Monthly percents =", round(finalSum * monthlyPercents, 2), end='\n\n')
