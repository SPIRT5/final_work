import pandas as pd
import random
# Создание данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание one-hot представления без get_dummies()
unique_values = data['whoAmI'].unique()
one_hot_columns = {}
for value in unique_values:
    one_hot_columns[f'{value}_onehot'] = (data['whoAmI'] == value).astype(int)

one_hot_df = pd.DataFrame(one_hot_columns)

# Объединение исходного DataFrame с one-hot представлением
data_one_hot = pd.concat([data, one_hot_df], axis=1)
data_one_hot.head(20)