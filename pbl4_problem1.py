# 2. import pandas


if __name__ == '__main__':
    ''' 
    3. Add a line of code to create a dataframe by reading the file from csv
    If you don't have the dataset saved in your project use the URL:
    https://raw.githubusercontent.com/nicholsons/comp0035_pbl4/master/data/paralympics_raw.csv?token=AHBUVRXMMNPI7VSWY4P34IDBO2TES'
    '''


    # Sets the pandas display options to the dimensions of the dataframe (if your dataframe is large this may not be
    # practical
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)

    # 4. Add a line of code to print the dataframe contents
