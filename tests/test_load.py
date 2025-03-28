import pytest
import pandas as pd
import os
from src.load import save_to_csv, zip_file

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'COD': ['123', '456'],
        'DESCRICAO': ['Procedimento A', 'Procedimento B']
    })

def test_save_to_csv(tmp_path, sample_data):
    # Testa salvar CSV
    csv_path = os.path.join(tmp_path, "test.csv")
    save_to_csv(sample_data, csv_path)
    
    assert os.path.exists(csv_path)
    
    # Verifica se o conteúdo está correto
    df_read = pd.read_csv(csv_path)
    pd.testing.assert_frame_equal(sample_data, df_read)

def test_zip_file(tmp_path, sample_data):
    # Primeiro cria um CSV para compactar
    csv_path = os.path.join(tmp_path, "to_zip.csv")
    zip_path = os.path.join(tmp_path, "test.zip")
    
    save_to_csv(sample_data, csv_path)
    zip_file(csv_path, zip_path)
    
    assert os.path.exists(zip_path)
    assert os.path.getsize(zip_path) > 0