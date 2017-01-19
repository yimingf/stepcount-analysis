import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
from scipy import stats

# parse xml and save to pandas-friendly file.
'''
tree = ET.parse('./export.xml')
root = tree.getroot()

for child in root.findall('Record'):
	if child.get('type') == 'HKQuantityTypeIdentifierStepCount':
		date = child.get('creationDate')
		step_count = child.get('value')
		print date, step_count
'''

# read and clean the data.
# step counts that are (less than 80) | (greater than 150) are considered meaningless data.
# reasons against those being counted:
# - less than 80 -> random wandering at home | slow walks
# - greater than 150 -> overlapping data (i cannot achieve 150spm lol)
df = pd.read_csv('./p.out', sep='\s+', header=None)
df = df.drop([1, 2], axis=1)
df = df[np.logical_and(df[3]>80, df[3]<150)]
df.columns = ['timestamp', 'count']
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df[df.timestamp >= pd.to_datetime('2016-05-23')]
df['in_china'] = np.logical_or(np.logical_and(df.timestamp >= pd.to_datetime('2016-05-23'), df.timestamp < pd.to_datetime('2016-09-25')), np.logical_and(df.timestamp >= pd.to_datetime('2016-12-16'), df.timestamp < pd.to_datetime('2017-01-15'))) * 1
# df.to_csv('./d.csv')

# make the mean/var analysis.
df[df['in_china'] == 0]['count'].mean() # 110.4 / 110.4
df[df['in_china'] == 1]['count'].mean() # 107.8 / 107.8
t_stat, p_value = stats.ttest_ind(df[df['in_china'] == 0]['count'], df[df['in_china'] == 1]['count'])
print(p_value) # 1e-22, significant!

sum = df.groupby(['timestamp'])['count', 'in_china'].sum()
sum['in_china'] = (sum['in_china'] > 0) * 1
sum[sum['in_china'] == 1]['count'].mean() # 5103.5
sum[sum['in_china'] == 0]['count'].mean() # 4435.7
t_stat, p_value = stats.ttest_ind(sum[sum['in_china'] == 1]['count'], sum[sum['in_china'] == 0]['count'])
print(p_value) # 0.14, not significant...