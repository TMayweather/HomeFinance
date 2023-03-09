import pandas as pd
import SendMessage as sm

# sm.send_message()

joint = pd.read_csv('/home/tmayweather/finance/jointjanfeb23.csv')
main = pd.read_csv('/home/tmayweather/finance/mainjanfeb23.csv')
df = pd.concat([joint, main], axis=0)
df.to_csv('fin.csv', index=False)
read_file = pd.read_excel('cc.xlsx')
print(df)
read_file.to_csv('cc.csv',
                 index=False,
                 header=True)
cc = pd.DataFrame(pd.read_csv('cc.csv', index_col=0))
print(cc)

start_date = ''
end_date = ''


def filter_date(start_date, end_date):
    date_mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    df_range = df.loc[date_mask]
    amounts_per_category = df_range.groupby('Category')['Amount'].sum()
    print(amounts_per_category)


filter_date('2023-01-01', '2023-01-31')























