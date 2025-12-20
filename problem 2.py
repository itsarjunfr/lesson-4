amt = int(input('Enter amount of money to be withdrawn: '))
note1 = amt//50
note2 = (amt%50)//10
note3 = ((amt%50)%10)//5
note4 = (((amt%50)%10)%5)//2

print('Number of $50 notes: ', note1)
print('Number of $10 notes: ', note2)
print('Number of $5 notes: ', note3)
print('Number of $2 notes: ', note4)