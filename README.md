# LLM Text Analyzer

A Python tool that reads .txt files, sends them to OpenAI API, and returns structured JSON.

## What it does

- Batch process multiple text files
- Call OpenAI API with custom prompts
- Save results as JSON files

## Use cases

- Sentiment analysis
- Financial report scoring
- Custom text classification


## Quick start

1. Install: `pip install openai`
2. Add your API key to `analyzer.py`
3. Put .txt files in `input/` folder
4. Run: `python analyzer.py`

## Example output

```json
{
  "sentiment": "positive",
  "score": 85,
  "key_phrases": ["great product", "fast delivery"],
  "summary": "User is very satisfied"
}
