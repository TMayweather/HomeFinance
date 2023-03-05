import calendar
import datetime
import pandas as pd
import SendMessage as sm

# sm.send_message()

j = pd.read_csv('jointjanfeb23.csv')
m = pd.read_csv('mainjanfeb23.csv')
c_payment = []
income = []
sum_income = 0
sum_c_payment = 0


cc_payments_df = j[j['Category'] == 'Credit Card Payment']
income_df = m[m['Category'] == 'Paycheck']



# Extract the values in the 'Amount' and 'Description' columns and append them to the c_payment list
def get_desc_amt():
    for index, row in cc_payments_df.iterrows():
        c_payment.append((row['Description'], row['Amount']))

    for index, row in income_df.iterrows():
        income.append((row['Description'], row['Amount']))


get_desc_amt()

for payment in c_payment:
    for e in payment:
        print(e)

for credit_cards in c_payment:
    c_name = credit_cards[0]
    c_amount = abs(credit_cards[1])
    print(f'The monthly payment made on {c_name} is ${c_amount}')

for paychecks in income:
    p_name = paychecks[0]
    p_amount = paychecks[1]
    sum_income += paychecks[1]


print(f'Our monthly income is ${sum_income}')


for payments in c_payment:
    sum_c_payment += abs(payments[1])

print(f'The total amount paid on Credit Cards is ${sum_c_payment}')






















