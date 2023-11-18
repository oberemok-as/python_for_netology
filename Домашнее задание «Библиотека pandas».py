#%%
import pandas as pd

#%% md
#Задание 1 \n
Датасет для домашнего задания вы найдете в разделе “Материалы к домашнему заданию” (файл “Дополнительные файлы для домашнего задания”) к этому занятию.
Определите, какому фильму было выставлено больше всего оценок 5.0.
#%%
data = pd.read_csv('https://drive.google.com/uc?id=1BzZZrTCb7xm2t8MLean_bbO5-7cVgyEi') # ratings.csv
data.head()
#%%
movies = pd.read_csv('https://drive.google.com/uc?id=1zUBnOeXyz_cKyzkFqlLa6SxVh_7fE6wH') # movies.csv
movies.head()

#%%
%%time
vyvod = data[ (data['rating']==5.0)].groupby('movieId').count().filter(items = ['movieId', 'rating']).sort_values('rating',ascending=False).head(1)


#%%
vyvod.merge(movies, on='movieId').head()
#%% md
#Задание 2 \n
По данным файла power.csv (находится в архиве в разделе Материалы к лекции «Библиотека Pandas» - файл “Дополнительные файлы для домашнего задания”) посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 год. Не учитывайте в расчётах отрицательные значения quantity.
#%%
power = pd.read_csv('https://drive.google.com/uc?id=135P-AOXgewgjRt88MaqDAq9Qy_M3Evm9') # power.csv
power.head()

#%%
power[ (power['country'].isin(['Latvia', 'Lithuania', 'Estonia'])) & (power['category'].isin([4,12,21])) & (power['year'] >= 2005) & (power['year'] <= 2010) & (power['quantity'] >= 0)].groupby('country').sum('quantity').filter(items = ['country', 'quantity']).head()
#%% md
#Задание 3 \n
Выберите страницу любого сайта с табличными данными. Импортируйте таблицы в pandas DataFrame. Вы можете взять любые страницы.
#%%
table_url = pd.read_html('https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html')[0]
table_url
#%%
type(table_url)