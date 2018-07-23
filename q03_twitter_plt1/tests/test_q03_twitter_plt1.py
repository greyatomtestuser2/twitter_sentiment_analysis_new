from unittest import TestCase
from ..build import q03_twitter_plt1
from inspect import getfullargspec
import pandas as pd

twitter_data=pd.read_csv('data.csv')      

def q02_tweet_info(twitter_data):
    tlen = pd.Series(data=twitter_data['len'].values, index=twitter_data['Date'])
    tfav = pd.Series(data=twitter_data['Likes'].values, index=twitter_data['Date'])
    tret = pd.Series(data=twitter_data['RTs'].values, index=twitter_data['Date'])

    return tlen, tfav, tret

q03_twitter_plt1(twitter_data)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q03_twitter_plt1).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

