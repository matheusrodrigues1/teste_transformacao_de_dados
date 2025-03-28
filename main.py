import os
from src.extract import extract_data_from_pdf
from src.transform import replace_abbreviations
from src.load import save_to_csv, zip_file
from src.utils import clean_data

def main(pdf_path: str, output_name: str) -> None:
    """
    Executa o pipeline completo de ETL
    
    Args:
        pdf_path (str): Caminho para o arquivo PDF de entrada
        output_name (str): Nome base para os arquivos de saída (seu_nome)
    """
    try:
        # Cria diretório de saída se não existir
        os.makedirs('data/output', exist_ok=True)
        
        # 1. Extração
        print("Extraindo dados do PDF...")
        df = extract_data_from_pdf(pdf_path)
        
        # Limpeza inicial
        df = clean_data(df)
        
        # 2. Transformação
        print("Transformando dados...")
        df = replace_abbreviations(df)
        
        # 3. Carga
        csv_path = f"data/output/{output_name}.csv"
        zip_path = f"data/output/Teste_{output_name}.zip"
        
        print(f"Salvando CSV em {csv_path}...")
        save_to_csv(df, csv_path)
        
        print(f"Criando arquivo ZIP em {zip_path}...")
        zip_file(csv_path, zip_path)
        
        print("Processo concluído com sucesso!")
    except Exception as e:
        print(f"Erro no processo principal: {e}")
        raise

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Processa PDF e gera CSV e ZIP")
    parser.add_argument("pdf_path", help="Caminho para o arquivo PDF")
    parser.add_argument("output_name", help="Seu nome para nomear o arquivo de saída")
    
    args = parser.parse_args()
    
    main(args.pdf_path, args.output_name)