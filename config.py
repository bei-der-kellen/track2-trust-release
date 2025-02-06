import os
from dotenv import load_dotenv

load_dotenv()

# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME", "o3-mini")

# Sensitivity Check Configuration
SENSITIVITY_RULES = {
    "personal_data": {
        "name": "Personal Data (GDPR Art. 4)",
        "description": "Information relating to identified or identifiable natural person"
    },
    "special_categories": {
        "name": "Special Categories (GDPR Art. 9)",
        "description": "Racial/ethnic origin, political opinions, religious beliefs, health data, etc."
    },
    "official_secrets": {
        "name": "Official Secrets (IFG §3)",
        "description": "Information classified as confidential by German law"
    },
    "business_secrets": {
        "name": "Business Secrets (IFG §6)",
        "description": "Trade secrets and confidential business information"
    }
} 