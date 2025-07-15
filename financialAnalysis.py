import pandas as pd

def financialAnalysis(df: pd.DataFrame) -> dict:
    salesColumns= 'Precio Venta Real'
    return {
        'totalSales': df[salesColumns].sum(),
        'averageSales': df[salesColumns].mean(),
        'statistics': df[salesColumns].describe()
    }

def salesBySegment(df: pd.DataFrame) -> pd.Series:
    return df.groupby('Segmento')['Precio Venta Real'].sum()