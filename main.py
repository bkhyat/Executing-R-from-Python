import numpy as np
import pandas as pd
import random

import rpy2.robjects
from scipy import stats
from rpy2 import robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter


def subprocess_(data):
    pass


def r_code(data):
    with localconverter(robjects.default_converter + pandas2ri.converter):
        data = robjects.conversion.py2ri(data)
    print(data)
    robjects.r('''
        counts <- as.data.frame.matrix(table(data))
        print(chisq.test(counts[1],  correct=FALSE))
        print(chisq.test(counts[2],  correct=FALSE))
    '''
    )


def python_code(data):
    # unique, count = np.unique(data, return_counts=True)
    # print('Flat Unique counts')
    # print(unique, count)
    # print('Chi squared result for flat frequency')
    # print(stats.chisquare(count))
    # cross_freq = pd.crosstab(data[0], data[1])
    cross_freq = pd.crosstab(data['SEX'], data['Flag'])
    print('Cross Frequency:')
    print(cross_freq)
    print('Chi squared result for cross frequency')
    print(stats.chisquare(cross_freq))


def get_chi_squared():
    print('Creating Random Dataframe')
    data = pd.DataFrame.from_dict({'SEX': np.array([random.choice(['F', 'M']) for _ in range(30)]),
                                   'Flag': np.array([random.choice([0, 1]) for _ in range(30)])})
    print(data)
    print('Calculating Chi Squared')
    print('Using Python with Scipy and Numpy')
    print('='.join('=' for _ in range(20)))
    python_code(data)
    print('='.join('=' for _ in range(20)))
    print('Using rpy2 with 3rd party wheel')
    r_code(data)
    print('='.join('=' for _ in range(20)))
    print('Using Python and R subprocess')
    subprocess_(data)


if __name__ == "__main__":
    get_chi_squared()