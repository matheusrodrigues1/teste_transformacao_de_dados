import pytest
import pandas as pd
from src.transform import replace_abbreviations

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'COD': ['123', '456'],
        'DESCRICAO': ['Procedimento A', 'Procedimento B'],
        'OD': ['OD', 'OD'],  # Valores originais
        'AMB': ['AMB', 'AMB']  # Valores originais
    })

@pytest.fixture
def expected_transformed_data():
    return pd.DataFrame({
        'COD': ['123', '456'],
        'DESCRICAO': ['Procedimento A', 'Procedimento B'],
        'OD': ['Seg. Odontológica', 'Seg. Odontológica'],  # Valores esperados
        'AMB': ['Seg. Ambulatorial', 'Seg. Ambulatorial']  # Valores esperados
    })

def test_replace_abbreviations(sample_data, expected_transformed_data):
    # Testa a substituição das abreviações
    transformed = replace_abbreviations(sample_data)
    
    pd.testing.assert_frame_equal(transformed, expected_transformed_data)
    
    # Testa com DataFrame sem as colunas OD e AMB
    df_no_columns = sample_data.drop(columns=['OD', 'AMB'])
    transformed_no_columns = replace_abbreviations(df_no_columns)
    pd.testing.assert_frame_equal(df_no_columns, transformed_no_columns)