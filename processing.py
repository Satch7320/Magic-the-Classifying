import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    df = pd.read_csv('data/en_cards.csv')
    # reset all values to strings, because every 'document (card)' should have the same fields
    df.fillna(value = '[none]', inplace = True)
    return df