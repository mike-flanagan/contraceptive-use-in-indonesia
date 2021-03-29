
def csv_write(ticker, df, start, end, intra = ''):
    '''Given a target filepath and a list of fields,
    create a new CSV file and set Headers
    '''
    df.columns = ['open', 'high', 'low', 'close', 'change', 'volume']
    if intra = 'y':
        intra = 'intra'
    csv_filepath = f'data/{ticker}_{intra}_{start}_{end}.csv'
    df.to_csv(csv_filepath, mode='w')
