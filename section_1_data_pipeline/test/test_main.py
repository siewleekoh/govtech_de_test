import pandas as pd
import pytest

from src.main import remove_titles, split_name


@pytest.fixture
def name_df():
    name_col = ['Mr. Joe Bloggs',
                  'Dr. Jane Smith',
                  'Mrs Alexis Andre',
                  'Mrs. Kelly Schmitt DVM',
                  'Joe Hood']
    price_col = ['0.00145',
                  '270.8972',
                  '205.98654 ',
                  '200.3679',
                  '0.007590']
    df_dict = {'name': name_col, 'price': price_col}
    df = pd.DataFrame(df_dict)
    return df


@pytest.fixture
def lowercased_name_df():
    name_col = ['joe bloggs', 'jane smith', 'alexis andre', 'kelly schmitt', 'joe hood']
    price_col = ['0.00145',
                  '270.8972',
                  '205.98654 ',
                  '200.3679',
                  '0.007590']
    df_dict = {'name': name_col, 'price': price_col}
    df = pd.DataFrame(df_dict)
    return df


def test_remove_titles(name_df):
    result = remove_titles(name_df)
    assert result['name'].tolist() == ['joe bloggs', 'jane smith', 'alexis andre', 'kelly schmitt', 'joe hood']


def test_split_name(lowercased_name_df):
    result = split_name(lowercased_name_df)
    assert result['first_name'].tolist() == ['Joe', 'Jane', 'Alexis', 'Kelly', 'Joe']
    assert result['last_name'].tolist() == ['Bloggs', 'Smith', 'Andre', 'Schmitt', 'Hood']

