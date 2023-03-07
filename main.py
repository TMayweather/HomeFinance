import pandas as pd
import re
import PyPDF2
import SendMessage as sm

# sm.send_message()

joint = pd.read_csv('jointjanfeb23.csv')
main = pd.read_csv('mainjanfeb23.csv')
df = pd.concat([joint, main], axis=0)
df.to_csv('fin.csv', index=False)
print(df)

start_date = '2023-01-01'
end_date = '2023-01-31'
date_mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
df_range = df.loc[date_mask]

amounts_per_category = df_range.groupby('Category')['Amount'].sum()
print(amounts_per_category)























