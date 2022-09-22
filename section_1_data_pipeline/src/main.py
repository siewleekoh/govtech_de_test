import pandas as pd
import numpy as np
import argparse
import os
from setup_logger import logger


class ETL:
    def __init__(self, csv_filepath, csv_filename):
        #self.logger = logging.getLogger(__name__)
        self.filepath = csv_filepath
        self.filename = csv_filename
        self.csv_fullpath = os.path.join(self.filepath, self.filename)
        self.processed_filename = 'processed' + '_' + self.filename

    def read_data(self):
        """
        Read a csv file;
        strip leading and trailing space of all columns.

        :param csv_file: csv file name
        :return: dataframe
        """

        df = pd.read_csv(self.csv_fullpath, sep=',', na_values='')

        column_names = ['name', 'price']
        for col in column_names:
            df[col] = df[col].astype(str).str.strip()

        return df

    def remove_titles(self, df):
        """
        Remove titles (in lower case) from names, remove leading and trailing spaces
        :param df: dataframe from csv file
        :return: dataframe with lower case name
        """

        name_titles = ['dr ', 'mr ', 'mrs ', 'ms ', ' jr', 'dds', 'dvm', 'md', 'phd']
        df['name'] = df['name'].str.lower()
        df['name'] = df.name.str.replace('.', '')
        df['name'] = df.name.replace({x: '' for x in name_titles}, regex=True)
        df['name'] = df['name'].str.strip()
        logger.info('Removed titles from name...')

        return df

    def split_name(self, df):
        """
        Split full name to first and last name.
        :param df: dataframe with titles removed from names
        :return: dataframe
        """
        df['first_name'] = df['name'].str.split(' ').str[0]
        df['first_name'] = df['first_name'].str.capitalize()

        df['last_name'] = df['name'].str.split(' ').str[1]
        df['last_name'] = df['last_name'].str.capitalize()

        logger.info('Split names to first and last name...')

        return df

    def add_above100(self, df):
        """
        Add a new column, 'above_100': assign value 'true' if 'price is > 100, else empty string.
        :param df:
        :return:
        """

        df['above_100'] = np.where(df['price'].astype('float') > 100, 'true', '')
        logger.info('Added "above_100" column to df...')

        return df

    def delete_empty_name(self, df):
        """
        Delete empty rows in 'name' column.
        :type df: object
        :param df:
        :return: pandas dataframe
        """
        # df[df['name'].astype(bool)]
        # df_new = df['name'].replace('', np.nan, inplace=True)
        # df.dropna(how='any', inplace=True)

        df_new = df[df['name'] != 'nan']
        logger.info('Removed empty name rows from df...')

        return df_new

    @staticmethod
    def write_csv(df, folder, out_filename):
        """
        Write a df to csv in to a folder location relative of the current working directory.
        :param df: pandas dataframe
        :param folder: name of the folder where the csv file should be
        :param out_filename: output csv file name
        :return: nothing
        """
        cwd = os.getcwd()
        path = os.path.join(cwd, folder)
        #ETL.logger.info(f'Writing to path {path}...')

        if not os.path.exists(path):
            os.makedirs(path)

        df.to_csv(os.path.join(path, out_filename), sep=',', index=False)

    def main(self):
        df_processed = self.read_data()
        if df_processed.shape[0] > 0:
            df_processed = self.delete_empty_name(df_processed)
            df_processed = self.remove_titles(df_processed)
            df_processed = self.split_name(df_processed)
            df_processed = self.add_above100(df_processed)
            self.write_csv(df_processed, '../output', self.processed_filename)
        else:
            logger.info('Data file is empty, exiting...')
            exit(1)

        return df_processed


if __name__ == "__main__":

    # add the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('Filepath', type=str,
                        help='The path to the csv file.')
    parser.add_argument('Filename', type=str,
                        help='The csv file name with file extension.')
    args = parser.parse_args()

    # parse arguments
    csv_file_path = args.Filepath
    csv_file_name = args.Filename

    try:
        etl_job = ETL(csv_file_path, csv_file_name)
        logger.info(f'File path: {csv_file_path}')
        logger.info(f'File name: {csv_file_name}')
        etl_job.main()
        logger.info(f'finished processing {csv_file_path}/{csv_file_name}...')
    except Exception as e:
        logger.error(f'An error has occurred, {e}')
