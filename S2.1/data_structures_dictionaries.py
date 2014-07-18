__author__ = 'ravi'
#initialize a couple of dictionaries
names = {'aisha':'ellahi', 'sara':'branco', 'melinda':'yang'}

drinks = {'emily':'milk', 'fernando':'coffee', 'jeff':'soda'}

wines = {'red':'cabernet','white':'pinot grigio','sparkling':'blanc de noirs', 'sticky':'muscato'}

print names,"\n", drinks, "\n", wines

print

print names['sara'], wines['sparkling'], drinks['fernando']

names.update(drinks)

print names

lst = [1,4,5,7]

