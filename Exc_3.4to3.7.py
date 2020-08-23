# 3.4

guests = ['Tony', 'Kevin', 'Holly']

print(guests[0] + ' I would like to invite you to our house warming party dinner.')
print(guests[1] + ' I would like to invite you to our house warming party dinner.')
print(guests[2] + ' I would like to invite you to our house warming party dinner.')

# 3.5

print(guests[-1] + ' Cannot make it to our party')

guests.remove('Holly')
guests.append('Chel')

print(guests[0] + ' I would like to invite you to our house warming party dinner.')
print(guests[1] + ' I would like to invite you to our house warming party dinner.')
print(guests[2] + ' I would like to invite you to our house warming party dinner.')

# 3.6

print(guests[0] + ' I found a bigger table, so I am going to invite 3 more friends.')
print(guests[1] + ' I found a bigger table, so I am going to invite 3 more friends.')
print(guests[2] + ' I found a bigger table, so I am going to invite 3 more friends.')

guests.insert(0, 'Dan')
guests.insert(2, 'Nikky')
guests.append('Cindy')
print(guests)

print(guests[0] + ' I would like to invite you to our house warming party dinner.')
print(guests[1] + ' I would like to invite you to our house warming party dinner.')
print(guests[2] + ' I would like to invite you to our house warming party dinner.')
print(guests[3] + ' I would like to invite you to our house warming party dinner.')
print(guests[4] + ' I would like to invite you to our house warming party dinner.')
print(guests[5] + ' I would like to invite you to our house warming party dinner.')

# 3.7

msg = ' I am sorry, you are being uninvited because I can only invite two people to the party.'

canceledguest0 = guests.pop(0)
print(canceledguest0 + msg)

canceledguest1 = guests.pop(1)
print(canceledguest1 + msg)

canceledguest2 = guests.pop(2)
print(canceledguest2 + msg)

canceledguest3 = guests.pop(2)
print(canceledguest3 + msg)

print(guests)

msg2 = ' I am happy to inform you that you are still being invited to the party.'

print(guests[0] + msg2)
print(guests[1] + msg2)

del guests[0]
del guests[1]
print(guests)
