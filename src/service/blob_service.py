import os
import streamlit as st
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from utils.config import Config


def upload_file_to_blob(file, file_name):
    try:
        connect_str = Config.CONNECTION_STRING
        container_name = Config.CONTAINER_NAME
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        blob_client.upload_blob(file, overwrite=True)
        
        blob_url = blob_client.url
        return blob_url 
    except Exception as e:
        st.error(f"Erro ao fazer upload para o Blob Storage: {e}")
        return None