import pandas as pd
from tabula import read_pdf

def extract_data_from_pdf(pdf_path: str) -> pd.DataFrame:
    """
    Extrai dados de tabelas de um PDF usando tabula-py
    
    Args:
        pdf_path (str): Caminho para o arquivo PDF
        
    Returns:
        pd.DataFrame: DataFrame com os dados extraídos
    """
    try:
        # Lê todas as tabelas do PDF
        dfs = read_pdf(pdf_path, pages='all', multiple_tables=True)
        
        # Combina todas as tabelas em um único DataFrame
        combined_df = pd.concat(dfs, ignore_index=True)
        
        return combined_df
    except Exception as e:
        print(f"Erro ao extrair dados do PDF: {e}")
        raise