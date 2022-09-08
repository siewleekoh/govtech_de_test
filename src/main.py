import pandas as pd
import numpy as np
import argparse


def read_data(csv_file):
    """
    Read a csv file;
    strip leading and trailing space of all columns.

    :param csv_file: csv file name
    :return: dataframe
    """

    df = pd.read_csv(csv_file, sep=',', na_values='')

    column_names = ['name', 'price']
    for col in column_names:
        df[col] = df[col].astype(str).str.strip()

    return df


def remove_titles(df):
    """
    Remove titles (in lower case) from names, remove leading and trailing spaces
    :param df: dataframe from csv file
    :return: dataframe with lower case name
    """

    name_titles = ['dr ', 'mr ', 'mrs ', 'ms ', ' jr', 'dds', 'dvm', 'md', 'phd']
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
    """
    Add a new column, 'above_100': assign value 'true' if 'price is > 100, else empty string.
    :param df:
    :return:
    """

    df['above_100'] = np.where(df['price'].astype('float') > 100, 'true', '')
    df.head()
    return df


def delete_empty_name(df):
    """
    Delete empty rows in 'name' column.
    :param df:
    :return:
    """
    # df[df['name'].astype(bool)]
    # df_new = df['name'].replace('', np.nan, inplace=True)
    df.dropna(how='any', inplace=True)

    # df_new = df[df['name'].notna()]

    return df


def main(csv_file):
    #df_processed = read_data('..\data\dataset2.csv')
    df_processed = read_data(csv_file)
    if df_processed.shape[0] > 0:
        df_processed = delete_empty_name(df_processed)
        df_processed = remove_titles(df_processed)
        df_processed = split_name(df_processed)
        df_processed = add_above100(df_processed)
        df_processed.head()
    else:
        print('Data file is empty, exiting...')
        exit(1)

    return df_processed


if __name__ == "__main__":

    # add the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('Filename', type=str,
                        help='The csv file name with file extension.')
    args = parser.parse_args()
    csv_filename = args.Filename
    print('filename:', csv_filename)

    try:
        main(csv_filename)
    except Exception as e:
        print(f'An error has occurred, {e}')
