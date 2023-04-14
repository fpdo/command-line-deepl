# Command-Line-DeepL
Allows user to translate sentences from English to Dutch using DeepL API and the command line

# Getting Started
1. `pip install -r requirements.txt`.
2. Create a `.env` file 
3. Head over to [DeepL](https://www.deepl.com/) create an accout, and copy your next API key.
4. Inside the `.env` file, create a variable called `API_KEY` and assign the key from #3.
  `API_KEY = "YOUR-API-KEY"`

Note: There are several tiers you can select when registering at Deepl. The current free tier offers up to 500.000 characters per month.

# How to use it
Add the `translate.py` script to your aliases.
```
alias deepl='path/to/repo/command-line-deepl/translate.py'
```

Then use the alias to translate any sentence you want.
```
deepl can you help me to get to the train station
```

If you don't want or can't add the script to your aliases, run it normally
lile any other python script.
```
python3 translate.py <sentence_to_translate>
```

# Linting
The project uses the python's Flake8 to check formatting style. It can be run locally by using.
```
flake8
```
And if there are violations they will be printed in the terminal.
