
def csv_write(ticker, df):
    '''Given a target filepath and a list of fields,
    create a new CSV file and set Headers
    '''
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    csv_filepath = f'data/{ticker}_intra_Mar_15_26.csv'
    df.to_csv(csv_filepath, mode='w')
