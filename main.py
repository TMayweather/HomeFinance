import pandas as pd

joint = pd.read_csv('/home/tmayweather/finance/jointjanfeb23.csv')
main = pd.read_csv('/home/tmayweather/finance/mainjanfeb23.csv')
df = pd.concat([joint, main], axis=0)
df.to_csv('fin.csv', index=False)


start_date = ''
end_date = ''


def filter_date(start_date, end_date):
    date_mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    df_range = df.loc[date_mask]
    amounts_per_category = df_range.groupby('Category')['Amount'].sum()
    print(amounts_per_category)


filter_date('2023-01-01', '2023-01-31')























