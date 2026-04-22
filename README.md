# LLM Text Analyzer

## What is this?

A Python script that reads text files, sends them to OpenAI, and returns structured JSON results.

**Think of it as:** You give it a bunch of .txt files and a set of rules. It asks ChatGPT to analyze each file and saves the results as organized JSON files.

## What can it do?

| Task | Example |
|------|---------|
| Sentiment analysis | "This product is great" → positive |
| Financial scoring | Earnings call → 0-100 score + key quotes |
| Custom analysis | Anything you define |

## How to use

### 1. Install Python and the package

```bash
pip install openai
