import pandas as pd

# Manipulação de dados
import pandas as pd
import numpy as np
import jinja2
# Visualização
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import missingno  # Visualização de dados faltantes

# Estatística
import scipy
from scipy.stats import normaltest
from scipy.stats import chi2_contingency

# Engenharia de Atributos
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
import category_encoders as ce

# Ignore Warning
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

# power bi
from powerbiclient import Report, models

# Import the DeviceCodeLoginAuthentication class to authenticate against Power BI
from powerbiclient.authentication import DeviceCodeLoginAuthentication

# notebook settings
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

# pandas settings
pd.set_option('display.max.rows', 3000)
pd.set_option('display.max.columns', 30)
pd.set_option('display.max_rows', 1200)

################
# Funções      #
################


def tipar_id(df):
    '''
    Define toda coluna que contem id_ como string
    '''
    for col in df.columns:
        if col.startswith('id_'):
            df[col] = df[col].astype(str)
    return df


def tipar_data(df):
    '''
    Define toda coluna que contem data_ como datetime
    '''
    for col in df.columns:
        if col.startswith('data_'):
            df[col] = pd.to_datetime(df[col])
    return df


def tipar_ano(df):
    '''
    Define toda coluna que contem ano_ como datetime
    '''
    for col in df.columns:
        if col.startswith('ano_'):
            df[col] = pd.to_datetime(df[col], format='%Y')
    return df


def valores_unicos(df):
    '''
    Exibe os valores unicos de cada coluna do dataframe
    '''
    for col in df.columns:
        print(f'Valores únicos para {col}: ', df[col].nunique())


def tipar_real(df):
    '''
    Define toda coluna que contem valor_ como float
    '''
    for col in df.columns:
        if col.startswith('valor_'):
            df[col] = df[col].astype(float)
