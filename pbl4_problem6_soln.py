# Problem 6: Joining data sets
import pandas as pd


# Set the pandas display options
def set_pandas_display_options(df):
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)


# Create a data frame with rows that have missing values and print it
def print_isna(df):
    df_isna = df[df.isna().any(axis=1)]
    print(df_isna)


if __name__ == '__main__':
    df = pd.read_csv('data/paralympics_raw.csv')
    set_pandas_display_options(df)

    # Drop the columns that we don't need
    df.drop(['Events', 'Sports', 'Countries'], axis=1, inplace=True)

    # Drop rows where there is a na in the Participants M or F columns
    df.dropna(axis=0, subset=['Participants (M)', 'Participants (F)'], inplace=True)

    # Replace the NaN in Type column with 'Winter'
    df.fillna({'Type': 'Winter'}, inplace=True)

    # Remove the extra spaces from 'Summer   '
    df['Type'] = df['Type'].str.strip()

    # Create a data frame with the the noc regions
    df_noc = pd.read_csv('data/noc_regions.csv')
    print(df_noc.columns)

    # Drop the 'notes' column
    df_noc.drop(['notes'], axis=1, inplace=True)
    print(df_noc.info(verbose=True))

    # Merge the columns where df['Country'] matches df_noc['region']
    df_merged = df.merge(df_noc, how='left', left_on='Country', right_on='region')
    df_merged.drop(['region'], axis=1, inplace=True)
    print(df_merged)
    print_isna(df_merged)


    # Manually add the 'NOC' code for Great Britain (GBR) and Republic of Korea (KOR)
    # This is a little more tricky as you need to replace a value in one column based on a condition in another
    # There will be more than one way to do this, I'm using a mask (condition).
    df_merged['NOC'].mask(df_merged['Country'] == 'Great Britain', 'GBR', inplace=True)
    df_merged['NOC'].mask(df_merged['Country'] == 'Republic of Korea', 'KOR', inplace=True)
    print_isna(df_merged)
