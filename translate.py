from dotenv import load_dotenv
import deepl
import os
import sys


class Translator:
    def __init__(self, prompt):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.deepl = deepl.Translator(self.api_key)
        if ("-" in prompt[0]):
            src_lang, dst_lang = prompt[0].split("-")
            self.prompt = " ".join(prompt[1:])
            # DeepL API needs the English version to be specificed
            if dst_lang == "EN" or dst_lang == "en":
                dst_lang += "-US"
            self.request(src_lang.upper(), dst_lang.upper())
        else:
            self.prompt = " ".join(prompt)
            self.request()

    def request(self, src_lang="EN", dst_lang="NL"):
        rsp = self.deepl.translate_text(self.prompt, source_lang=src_lang,
                                        target_lang=dst_lang)
        print(rsp.text)


obj = Translator(sys.argv[1:])
