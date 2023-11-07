# -*- coding: utf-8 -*-
"""Feature_Selection_risk _category.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T5sAtLSmeQmJg_rivNMK6NwmKAF9ptBm
"""

import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ttest_ind

from scipy import stats


"""methylation"""

df_mirna = pd.read_csv("/content/drive/MyDrive/omicData/miRNA_risk_category.csv",index_col=0)
df_mirna

df_mirna['acute_myeloid_leukemia_calgb_cytogenetics_risk_category'] = df_mirna['acute_myeloid_leukemia_calgb_cytogenetics_risk_category'].map({'Intermediate/Normal': 0, 'Favorable': 0,'Poor':1,'NA':-1})

df_mirna

df1_mirna = df_mirna.loc[df_mirna['acute_myeloid_leukemia_calgb_cytogenetics_risk_category'] == 0.0]
df1_mirna.to_csv('miRNA_risk_category_intermediate_normal_favorable.csv')

df2_mirna = df_mirna.loc[df_mirna['acute_myeloid_leukemia_calgb_cytogenetics_risk_category'] == 1.0]
df2_mirna.to_csv('miRNA_risk_category_poor.csv')

methy= pd.read_csv(r"/content/drive/MyDrive/omicData/miRNA.csv",index_col=0)
methy

sample_1_methy=methy.T
sample_1_methy

miRNA_risk_category_intermediate_normal_favorable = pd.read_csv("/content/drive/MyDrive/omicData/miRNA_risk_category_intermediate_normal_favorable.csv",index_col=0)

miRNA_risk_category_intermediate_normal_favorable

sample_2_methy_normal = miRNA_risk_category_intermediate_normal_favorable

from statsmodels.stats.weightstats import ttest_ind
import numpy as np
from scipy import stats
ttest_ind(sample_1_methy, sample_2_methy_normal)

t3_methy,p3_methy = stats.ttest_ind(sample_1_methy, sample_2_methy_normal) 
t3_methy,p3_methy

count1 = 0
for x in p3_methy:
  if x < 0.001:
    count1+=1
print("miRNA_risk_category_intermediate_normal_favorable :",count1)

miRNA_risk_category_poor = pd.read_csv("/content/drive/MyDrive/omicData/miRNA_risk_category_poor.csv",index_col=0)

miRNA_risk_category_poor

sample_2_methy_poor = miRNA_risk_category_poor

t3_methy_poor,p3_methy_poor = stats.ttest_ind(sample_1_methy, sample_2_methy_poor) 
t3_methy_poor,p3_methy_poor

count = 0
for x in p3_methy_poor:
  if x < 0.001:
    count+=1
print("miRNA_risk_category_poor :",count)

