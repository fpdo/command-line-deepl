from dotenv import load_dotenv
import deepl
import os
import sys


class Translator:
    def __init__(self, prompt):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.prompt = " ".join(prompt)
        self.deepl = deepl.Translator(self.api_key)
        self.request()

    def request(self):
        rsp = self.deepl.translate_text(self.prompt, source_lang="EN",
                                        target_lang="NL")
        print(rsp.text)


obj = Translator(sys.argv[1:])
