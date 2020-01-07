nameList = ["Juan", "Rae", "Ivanna", "Lilly", "Robert"]
wageList = [7.50, 11.00, 18.25, 9.25, 11.10]
hoursList = [35, 41, 26, 35, 45]
x = 0

while x < len(nameList):
    # calculate overtime
    if hoursList[x] > 40:
        grossPay = (35*wageList[x]) + (hoursList[x]-35)*(wageList[x]*1.5)
    else:
        # calculate regular time
        grossPay = hoursList[x]*wageList[x]
        
    
    print(nameList[x], wageList[x], hoursList[x], grossPay)
    x += 1

for x in range(len(nameList)):
    if hoursList[x] > 40:
        # calculate overtime
        grossPay = (35*wageList[x]) + (hoursList[x]-35)*(wageList[x]*1.5)
    else:
        # calculate regular time
        grossPay = hoursList[x]*wageList[x]
    
    print(nameList[x], wageList[x], hoursList[x], grossPay)
    
