ticket_1 = 0
ticket_2 = 40
ticket_3 = 30
ticket_4 = 25
ticket_5 = 20

if ticket_1 > ticket_2 and ticket_1 > ticket_3 and ticket_1 > ticket_4 and ticket_1 > ticket_5:
    print('1')
elif ticket_2 > ticket_1 and ticket_2 > ticket_3 and ticket_2 > ticket_4 and ticket_2 > ticket_5:
    print('2')
elif ticket_3 > ticket_2 and ticket_3 > ticket_1 and ticket_3 > ticket_4 and ticket_3 > ticket_5:
    print('3')
elif ticket_4 > ticket_2 and ticket_4 > ticket_3 and ticket_4 > ticket_1 and ticket_4 > ticket_5:
    print('4')
elif ticket_5 > ticket_2 and ticket_5 > ticket_3 and ticket_5 > ticket_4 and ticket_5 > ticket_1:
    print('5')