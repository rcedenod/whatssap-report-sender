import pandas as pd

def readSalesData(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, engine='openpyxl')
    return df