from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.config import Config

def analyze_document(card_url):
    endpoint = Config.ENDPOINT
    api_key = Config.API_KEY

    try:
        client = DocumentIntelligenceClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(api_key)
        )

        card_info = client.begin_analyze_document(
            "prebuilt-creditCard",
            AnalyzeDocumentRequest(url_source=card_url)
        ).result()
        
        for document in card_info.documents:
            fields = document.get("fields", {})
            result = {
                "card_name": fields.get("cardHolderName").get("content") if fields.get("cardHolderName") else None,
                "card_number": fields.get("cardNumber").get("content") if fields.get("cardNumber") else None,
                "expiry_date": fields.get("expirationDate").get("content") if fields.get("expirationDate") else None,
                "cvv": fields.get("cvv").get("content") if fields.get("cvv") else None,
            }
       
        return result
    except Exception as e:
        print(f"Error analyzing document: {e}")
        return None