import ast
import sys
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

changes_text = open(sys.argv[1]).read()
response = openai.Completion.create(
                model="text-davinci-003",
                prompt="commit ",
                suffix="\n\n" + changes_text,
                temperature=0,
                max_tokens=128,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0)
splits = response.choices[0].text.split("\n")
if len(splits) >= 5:
    print(splits[4].lstrip())
