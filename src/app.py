import streamlit as st
from service.blob_service import upload_file_to_blob
from service.card_service import analyze_document

def configure_interface():
    st.title("Upload de Arquivo DIO - Credit Card Scanner")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpeg", "jpg"])
    
    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = upload_file_to_blob(uploaded_file, fileName)
        if blob_url is not None:
            st.success(f"Arquivo '{fileName}' carregado com sucesso!")
            st.write(f"URL do Blob: {blob_url}")
            credit_card_info = analyze_document(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.error("Erro ao carregar o arquivo.")
            
def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem Carregada", use_container_width =True)
    st.write("Informações do Cartão de Crédito:")
    if credit_card_info and credit_card_info["card_name"]:
        st.write(f"Nome no Cartão: {credit_card_info['card_name']}")
        st.write(f"Número do Cartão: {credit_card_info['card_number']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
        st.write(f"Código CVV: {credit_card_info['cvv']}")
    else:
        st.write("Nenhuma informação de cartão de crédito encontrada.")
    
if __name__ == "__main__":
    configure_interface()
    