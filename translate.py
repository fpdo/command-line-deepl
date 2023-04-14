from dotenv import load_dotenv
import requests
import sys
import os


class Translator:
    def __init__(self, prompt):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.url = "https://api-free.deepl.com/v2/translate"
        self.prompt = " ".join(prompt)
        self.prepare_request()
        rsp = self.forward_request()
        if (type(rsp) == int):
            return
        else:
            self.parse_response(rsp)

    def prepare_request(self):
        self.data = {
            "auth_key": self.api_key,
            "text": self.prompt,
            "source_lang": "EN",
            "target_lang": "NL"
        }

    def forward_request(self):
        response = requests.post(self.url, data=self.data)
        if (response.status_code == 200):
            response_data = response.json()
            return response_data
        else:
            print(f"Something went wrong.... request returned with status code\
                  {response.status_code}")
            return -1

    def parse_response(self, rsp):
        translated_text = rsp['translations'][0]['text']
        print(translated_text)


obj = Translator(sys.argv[1:])
