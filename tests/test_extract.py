import pytest
import pandas as pd
from src.extract import extract_data_from_pdf
import os

@pytest.fixture
def sample_pdf_path():
    return "data/input/sample.pdf"  # Você deve criar um PDF de teste pequeno

def test_extract_data_from_pdf(sample_pdf_path):
    # Testa se a função retorna um DataFrame
    df = extract_data_from_pdf(sample_pdf_path)
    assert isinstance(df, pd.DataFrame)
    
    # Testa se o DataFrame não está vazio
    assert not df.empty
    
    # Testa se a função levanta exceção com arquivo inválido
    with pytest.raises(Exception):
        extract_data_from_pdf("caminho/inexistente.pdf")