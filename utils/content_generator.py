import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class ContentGenerator:
    def __init__(self):
        self.api_key = os.getenv('LYZR_API_KEY')
        self.base_url = 'https://agent-prod.studio.lyzr.ai/v3/inference/'
        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': self.api_key
        }
    
    def generate_post_ideas(self, topic, audience):
        payload = {
            "user_id": "user@example.com",
            "agent_id": "676cb130dec1ba012db54066",
            "session_id": "676cb130dec1ba012db54066",
            "message": f"Generate LinkedIn post ideas about {topic} for {audience}"
        }
        
        response = requests.post(
            self.base_url,
            headers=self.headers,
            json=payload
        )
        
        return response.json()
    
    def create_content_calendar(self, topics, frequency):
        payload = {
            "user_id": "user@example.com",
            "agent_id": "676cb130dec1ba012db54066",
            "session_id": "676cb130dec1ba012db54066",
            "message": f"Create a content calendar for topics: {topics} with posting frequency: {frequency}"
        }
        
        response = requests.post(
            self.base_url,
            headers=self.headers,
            json=payload
        )
        
        return response.json()