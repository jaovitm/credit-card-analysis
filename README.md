# Credit Card Scanner 💳

Este projeto é uma aplicação web desenvolvida em Python com Streamlit que permite aos usuários fazer o upload de uma imagem de cartão de crédito. A aplicação utiliza os serviços de IA da Azure para extrair e exibir as informações do cartão, como nome do titular, número, data de validade e CVV.

## 📖 Descrição

O objetivo principal é demonstrar a integração de uma aplicação web com os serviços cognitivos da Azure, especificamente o **Document Intelligence** para análise de documentos e o **Blob Storage** para armazenamento de arquivos.

## ✨ Funcionalidades

-   **Upload de Imagem**: Interface para carregar arquivos de imagem (`.png`, `.jpeg`, `.jpg`).
-   **Armazenamento em Nuvem**: As imagens são enviadas para um container no Azure Blob Storage.
-   **Análise com IA**: O serviço Azure Document Intelligence é utilizado para analisar a imagem e extrair os dados do cartão de crédito.
-   **Visualização**: A imagem e as informações extraídas são exibidas na tela.

## 🛠️ Tecnologias Utilizadas

-   **Linguagem**: Python 3
-   **Framework Web**: Streamlit
-   **Serviços Azure**:
    -   Azure Blob Storage
    -   Azure Document Intelligence
-   **Bibliotecas Python**:
    -   `streamlit`
    -   `azure-storage-blob`
    -   `azure-ai-documentintelligence`
    -   `python-dotenv`

## ⚙️ Pré-requisitos

-   Python 3.8 ou superior
-   Uma conta na Azure com as seguintes configurações:
    -   Um serviço de **Armazenamento de Blobs**.
    -   Um serviço de **Document Intelligence**.

## 🚀 Instalação e Execução

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DA_PASTA_DO_PROJETO>
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r docs/src/requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo chamado `.env` na pasta `docs/src/` e adicione suas credenciais da Azure:
    ```env
    CONNECTION_STRING="Sua_Connection_String_do_Blob_Storage"
    CONTAINER_NAME="Nome_do_Seu_Container"
    ENDPOINT="Seu_Endpoint_do_Document_Intelligence"
    API_KEY="Sua_API_Key_do_Document_Intelligence"
    ```

5.  **Execute a aplicação:**
    Navegue até a pasta `docs/src/` e execute o seguinte comando no terminal:
    ```bash
    streamlit run app.py
    ```

A aplicação estará disponível no seu navegador no endereço `http://localhost:8501`.
