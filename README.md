## Teste de Transformação de Dados

Este projeto realiza a extração de dados de tabelas em arquivos PDF, transforma esses dados substituindo abreviações por suas descrições completas, e gera arquivos estruturados em CSV compactados. O objetivo é automatizar o processo de transformação de dados de documentos PDF para formatos mais acessíveis e manipuláveis.

## Estrutura do Projeto

teste_transformacao_dados/</br>
├── main.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Script principal para executar o pipeline completo</br>
├── requirements.txt &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Lista de dependências do projeto</br>
├── README.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Documentação do projeto</br>
├── src/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Código-fonte do projeto</br>
│ ├── **init**.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Define o diretório como módulo Python</br>
│ ├── extract.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Módulo para extração de dados do PDF</br>
│ ├── transform.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Módulo para transformação dos dados</br>
│ ├── load.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Módulo para carga dos dados (CSV e ZIP)</br>
│ └── utils.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Funções utilitárias auxiliares</br>
├── data/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Diretório para armazenar os arquivos de entrada/saída</br>
│ ├── input/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Arquivos PDF originais</br>
│ └── output/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Arquivos gerados (CSV, ZIP)</br>
└── tests/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Testes automatizados</br>
├── **init**.py
├── test_extract.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Testes para extract.py</br>
├── test_transform.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Testes para transform.py</br>
└── test_load.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Testes para load.py</br>

## Como executar

1. **Clone o repositório**:

   Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/matheusrodrigues1/teste_transformacao_de_dados
   cd web_scraping_project
   ```

2. Configuração do Ambiente Virtual (venv):

   ```bash
     python -m venv venv
     source venv/bin/activate  # No Linux/Mac
     # ou
     venv\Scripts\activate     # No Windows

   ```

3. Instale as dependências:

   ```bash
     pip install -r requirements.txt

   ```

4. Execute o script principal:
   ```bash
     python main.py data/input/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf "Seu_Nome"
   ```

O script irá:

Extrair os dados do PDF

Substituir as abreviações (OD → "Seg. Odontológica", AMB → "Seg. Ambulatorial")

Salvar os dados em CSV

Compactar o CSV em um arquivo ZIP

Arquivos gerados:

CSV transformado: data/output/Seu_Nome.csv

Arquivo compactado: data/output/Teste_Seu_Nome.zip

## Funcionalidades Principais

### Módulos:

1. extract.py:

   Extrai tabelas de arquivos PDF usando a biblioteca tabula-py

   Combina múltiplas tabelas em um único DataFrame

2. transform.py:

   Substitui abreviações pelas descrições completas:

   OD → Seg. Odontológica

   AMB → Seg. Ambulatorial

   Realiza limpeza básica dos dados

3. load.py:

   Salva os dados em formato CSV

   Compacta o CSV em arquivo ZIP

4. utils.py:

   Funções auxiliares para limpeza e tratamento de dados

## Testes Automatizados

Para executar os testes:

```bash
pytest tests/test_transform.py
```

Os testes cobrem:

- Extração de dados de PDF (com mock)

- Transformação de abreviações

- Geração de arquivos CSV e ZIP

## Dependências

Principais bibliotecas utilizadas:

- pandas: Manipulação de dados

- tabula-py: Extração de tabelas de PDF

- pytest: Framework de testes

#### Desde já agradeço a oportunidade
