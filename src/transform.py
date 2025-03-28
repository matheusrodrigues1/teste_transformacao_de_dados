import pandas as pd

def replace_abbreviations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Substitui as abreviações OD e AMB pelas descrições completas
    
    Args:
        df (pd.DataFrame): DataFrame com os dados originais
        
    Returns:
        pd.DataFrame: DataFrame com as abreviações substituídas
    """
    try:
        # Verifica se as colunas existem no DataFrame
        if 'OD' in df.columns:
            df['OD'] = df['OD'].replace({
                'OD': 'Seg. Odontológica',
            })
        
        if 'AMB' in df.columns:
            df['AMB'] = df['AMB'].replace({
                'AMB': 'Seg. Ambulatorial',
            })
            
        return df
    except Exception as e:
        print(f"Erro ao substituir abreviações: {e}")
        raise