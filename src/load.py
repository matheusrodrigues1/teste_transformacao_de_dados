import pandas as pd
import zipfile
import os

def save_to_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Salva o DataFrame em um arquivo CSV
    
    Args:
        df (pd.DataFrame): DataFrame a ser salvo
        output_path (str): Caminho para o arquivo de saída
    """
    try:
        df.to_csv(output_path, index=False)
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")
        raise

def zip_file(input_path: str, output_path: str) -> None:
    """
    Compacta um arquivo em ZIP
    
    Args:
        input_path (str): Caminho do arquivo a ser compactado
        output_path (str): Caminho do arquivo ZIP de saída
    """
    try:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(input_path, os.path.basename(input_path))
    except Exception as e:
        print(f"Erro ao criar arquivo ZIP: {e}")
        raise