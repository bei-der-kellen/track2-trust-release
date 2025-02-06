import json
from config import SENSITIVITY_RULES
import re

class SensitivityChecker:
    @staticmethod
    def check_document(text_content, ai_processor):
        """
        Check document content for sensitive information.
        Returns list of sensitive sections with their categories and locations.
        """
        sensitive_sections = []
        
        # Process each page
        for page_num, page_text in enumerate(text_content):
            analysis = ai_processor.analyze_text(page_text)
            
            try:
                results = json.loads(analysis)
                for section in results.get('sensitive_sections', []):
                    sensitive_sections.append({
                        'page_num': page_num,
                        'text': section['text'],
                        'category': section['category'],
                        'reason': section['reason'],
                        'accepted': False  # Will be updated by user
                    })
            except json.JSONDecodeError:
                print(f"Error parsing AI response for page {page_num}")
                
        return sensitive_sections 

def find_sensitive_info(text):
    sensitive_ranges = []
    
    # Patterns for sensitive information
    patterns = {
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
        'credit_card': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
    }
    
    for sensitivity_type, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            sensitive_ranges.append({
                'start': match.start(),
                'end': match.end(),
                'type': sensitivity_type,
                'text': match.group()
            })
    
    return sensitive_ranges 