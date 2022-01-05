from rpy2 import robjects
from rpy2.robjects.packages import importr
base = importr('base')
stat = importr('stats')
import pandas as pd
import numpy as np
import random
data = pd.DataFrame.from_dict({'SEX': np.array([random.choice(['F', 'M']) for _ in range(30)]),
                               'Flag': np.array([random.choice([0, 1]) for _ in range(30)])})

from rpy2.robjects import pandas2ri
with robjects.conversion.localconverter(robjects.default_converter + pandas2ri.converter):
    df = robjects.conversion.py2rpy(data)
out=base.as_data_frame(base.table(robjects.conversion.py2rpy(df)))
res=stat.chisq_test(out)
print(res)


