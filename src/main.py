import pandas as pd


def read_data(csv_file):
    """
    Read a csv file;
    strip leading and trailing space of all columns.

    :param csv_file: csv file name
    :return: dataframe
    """

    df = pd.read_csv(csv_file, sep=',')

    column_names = ['name', 'price']
    for col in column_names:
        df[col] = df[col].astype(str).str.strip()

    return df


def remove_titles(df):
    """
    Remove titles from names.
    :param df: dataframe from csv file
    :return: dataframe
    """
    name_titles = ['dr', 'mr', 'mrs', 'ms', 'jr', 'dds', 'dvm', 'md', 'phd']
    df['name'] = df['name'].str.lower()
    df['name'] = df.name.str.replace('.', '')
    df['name'] = df.name.replace({x:'' for x in name_titles}, regex=True)
    df['name'] = df['name'].str.strip()

    return df


def split_name(df):
    """
    Split full name to first and last name.
    :param df: dataframe with titles removed from names
    :return: dataframe
    """
    df['first_name'] = df['name'].str.split(' ').str[0]
    df['first_name'] = df['first_name'].str.capitalize()

    df['last_name'] = df['name'].str.split(' ').str[1]
    df['last_name'] = df['last_name'].str.capitalize()

    return df


def add_above100(df):
    pass


def delete_empty_name(df):
    pass


def main():
    df_processed = read_data('..\data\dataset1.csv')
    df_processed = remove_titles(df_processed)
    df_processed = split_name(df_processed)
    df_processed.head()

    return df_processed


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print(f'An error has occurred, {e}')
