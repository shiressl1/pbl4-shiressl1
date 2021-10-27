# Problem 4: Identify and address any missing values
import pandas as pd


# Set the pandas display options
def set_pandas_display_options(df):
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)


if __name__ == '__main__':

    df = pd.read_csv('data/paralympics_raw.csv')
    set_pandas_display_options(df)
    df = df.drop(['Events', 'Sports', 'Countries'], axis=1)

    # Find the number of missing values
    # print(df.isnull().sum().sum())
    print(df.isna().sum().sum())

    # Print rows with missing values
    print(df[df.isna().any(axis=1)])

    # Drop rows where there is a NaN in the Participants M or F columns
    df.dropna(axis=0, subset=['Participants (M)', 'Participants (F)'], inplace=True)
    print(df.isna().sum().sum())

    # Replace the NaN in Type column with 'Winter'
    df.fillna({'Type': 'Winter'}, inplace=True)
    print(df.isna().sum().sum())
