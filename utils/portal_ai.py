from langchain_ai_portal import UbitecAiPortalSdkChat
from langchain_core.messages import HumanMessage, SystemMessage
import os

class PortalAIProcessor:
    def __init__(self):
        # Load the Portal API endpoint and key from environment variables (.env)
        self.host = os.getenv("PORTAL_API_HOST")
        self.port = os.getenv("PORTAL_API_PORT")
        self.api_key = os.getenv("PORTAL_API_API_KEY")
        self.use_ssl = os.getenv("PORTAL_API_USE_SSL")
        self.model_identifier = os.getenv("PORTAL_API_MODEL_IDENTIFIER")

    async def get_completion(self, prompt):
        system_message = "Du bist ein Assistent, welcher auf Deutsch antwortet."
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=prompt)
        ]
        response = await self.chat_model.ainvoke(messages)
        return response.content

    async def analyze_text(self, text):
        """
        Analyze the provided text for sensitive information.
        This method wraps `get_completion` so it has the same interface as AzureAIProcessor.
        """
        prompt = """
        Analyze the following text for sensitive information according to GDPR and German 
        Informationsfreiheitsgesetz (IFG). Identify any:
        1. Personal data (names, addresses, contact info)
        2. Special category data (health, religion, political opinions)
        3. Official secrets
        4. Business secrets or confidential information
        
        Return the results in the following JSON format:
        {
            "sensitive_sections": [
                {
                    "text": "sensitive text excerpt",
                    "category": "category name",
                    "reason": "explanation why this is sensitive"
                }
            ]
        }
        Just give back the JSON and nothing else. Don't add any comments or explanations. Don't say "Here is the JSON" or anything like that.
        Text to analyze:
        """ + text
        return await self.get_completion(prompt) 