from openai import OpenAI  # Ensure you have openai installed (pip install openai)
import os

class AlbertAIProcessor:
    def __init__(self):
        # Load the Albert API endpoint and key from environment variables (.env)
        self.base_url = os.getenv("ALBERT_ENDPOINT", "https://albert.api.etalab.gouv.fr/v1")
        self.api_key = os.getenv("ALBERT_API_KEY", "your_albert_api_key_here")
        self.client = OpenAI(base_url=self.base_url, api_key=self.api_key)

    def get_completion(self, prompt, model="AgentPublic/llama3-instruct-guillaumetell"):
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "n": 1,
        }
        response = self.client.chat.completions.create(**data)
        #print(response.choices[0].message.content)
        return response.choices[0].message.content

    def analyze_text(self, text):
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
        return self.get_completion(prompt) 