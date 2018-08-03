import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

# Read the data set into a pandas DataFrame
iris = pd.read_csv('iris.csv', sep=',', header=0)

print('''빅데이터 로드중..
분석용 빅데이터 가공중..
빅데이터 통게 분석 모델 생성중..''')
iris.columns = [heading.lower() for heading in iris.columns.str.replace('.', '_')]

iris['const'] = np.where(iris['variety'] == 'Setosa', 1., 0.)

dependent_variable = iris['const']
independent_variables = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()
print('''테스트 데이터 선별 중..

샘플링 데이터 예측 테스트 중
6개 샘플링 데이터 리스트''')
i_var=iris[['const', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
sample = iris.ix[iris.index.isin(range(48,54)), i_var.columns]
print(sample)
print('예측결과 분석 중')
