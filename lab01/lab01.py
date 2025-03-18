temperature = int(input('Temperature in degrees: '))
budget = float(input('Budget in dollars: '))
weathercondition = str(input('Weather condition - sunny, rainy, or cloudy: ')).lower()

if (weathercondition == 'sunny') and (temperature > 75): 
    if (budget > 20.0):
        print('Go to the beach!')
    else: 
        print('Have a picnic in the park.')
elif (weathercondition == 'rainy'): 
    if (budget > 15.0): 
        print('Visit a museum')
    else:
        print('Stay in and watch a movie at home.')
elif (weathercondition == 'cloudy') or (temperature < 60):
    print('Go to a coffee shop and enjoy a warm drink.')
else: 
    print('No suggestions. Enter sunny, rainy or cloudy.')