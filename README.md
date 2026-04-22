# LLM Text Analyzer

## Sample Output

```json
{
  "composite_score": 78,
  "signal_stage": "positive",
  "key_quotes": [
    "Services revenue reached an all-time high",
    "AI initiatives are gaining strong momentum"
  ],
  "risk_flags": [
    "Softness in China market"
  ]
}
What it does
Reads .txt files → sends to OpenAI API → returns structured JSON.

Use cases
Financial report scoring (0-100 + key quotes + risk flags)

Sentiment analysis (positive/neutral/negative)

Custom text analysis

Quick start
bash
# 1. Install dependency
pip install openai

# 2. Set your API key in analyzer.py

# 3. Put .txt files in 'input' folder

# 4. Run
python analyzer.py
Example
Input (input/sample.txt):

text
Apple Q4 2024 Earnings Call
CEO: Services revenue hit all-time high. AI momentum is strong.
CFO: However, we see softness in China market.
Output (output/sample_analysis.json):

json
{
  "composite_score": 78,
  "signal_stage": "positive",
  "key_quotes": [
    "Services revenue hit all-time high",
    "AI momentum is strong"
  ],
  "risk_flags": [
    "Softness in China market"
  ]
}
Customize
Edit SYSTEM_PROMPT in analyzer.py to change the analysis rules.

Requirements
Python 3.9+

OpenAI API key

Files
File	Description
analyzer.py	Main script
requirements.txt	Dependencies
input/	Put your .txt files here
output/	Results saved here
