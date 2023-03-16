#!/usr/bin/env python3

from asterisk.agi import AGI
import openai
import sys

openai.api_key = "<key>"


agi = AGI()

agi.set_variable("hass_text", "")

voiceText = sys.argv[1]
agi.verbose(f"Asking for: {voiceText}")
response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[{"role": "user", "content": voiceText}])
answer = response.choices[0].message.content.strip().replace(",",".").replace("\n",".").strip()
agi.verbose(f"Recognized: {answer}") 
agi.set_variable("hass_text", answer)
