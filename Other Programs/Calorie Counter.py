'''
Calorie Counter
'''
#Breckfast
breckfast = {
       'friedegg':92,
       'wheatabix':68,
       'toast':98,
       'porridge':148
       }

#School Lunches
school = {
        'hamsandwich':241,
        'chickensandwich':339,
        'hamcheesesandwich':339,
        'hamwrap':233,
        'chickenwrap':331,
        'hamcheesewrap':331,
        'oatcakes':290,
        'banana':95,
        'apple':49
        }

#common meals (Per Portion)
meals = {
        'tortilla':956,
        'dinner':1000,
        'chips':4040
        }

#items measured by amount (Cals per 1 piece)
amount = {
        'apple':49,
        'banana':95,
        'bread':98,
        'wrap':189
        }






print('Enter The Number Of Items You Wish To Input')

n = int(input())

print('Enter The Food You Ate Today')

foods = dict((map(str, input().split())) for x in range(n))

total = []

for key in foods:
    if key in breckfast:
        print(int(breckfast[key]) * int(foods[key]), 'cals')
        total.append(int(breckfast[key]) * int(foods[key]))

    if key in school:
        print(int(school[key]) * int(foods[key]), 'cals')
        total.append(int(school[key]) * int(foods[key]))

    if key in meals:
        print(int(meals[key]) * int(foods[key]), 'cals')
        total.append(int(meals[key]) * int(foods[key]))

    if key in amount:
        print(int(amount[key]) * int(foods[key]), 'cals')
        total.append(int(amount[key]) * int(foods[key]))

        

print(('Total:'),sum(total),('cals'))

min_cals = 2000
max_cals = 3200

if sum(total) > min_cals and sum(total) < max_cals:
    print('You have eaten inside the correct range :)')

if sum(total) < min_cals:
    print('You were', min_cals - sum(total),'under the minimum ammount :(')    

if sum(total) > max_cals:
    print('You ate', sum(total) - max_cals, 'cals over the maximum ammount :(')



