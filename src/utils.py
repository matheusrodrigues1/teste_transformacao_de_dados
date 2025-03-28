import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa o DataFrame removendo linhas vazias e ajustando tipos de dados
    
    Args:
        df (pd.DataFrame): DataFrame original
        
    Returns:
        pd.DataFrame: DataFrame limpo
    """
    # Remove linhas totalmente vazias
    df = df.dropna(how='all')
    
    # Remove espaços em branco dos nomes das colunas
    df.columns = df.columns.str.strip()
    
    return df