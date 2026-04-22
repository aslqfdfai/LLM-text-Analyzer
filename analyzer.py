"""
LLM Text Analyzer - Batch text analysis with OpenAI API
Usage:
1. pip install openai
2. Set your API key below
3. Put .txt files in 'input' folder
4. Run: python analyzer.py
"""

import json
import os
from pathlib import Path
from openai import OpenAI

# ===== CONFIGURATION =====
API_KEY = "your-api-key-here"  # Replace with your OpenAI API key
INPUT_FOLDER = "input"          # Folder for input .txt files
OUTPUT_FOLDER = "output"        # Folder for output JSON files

# ===== INITIALIZATION =====
client = OpenAI(api_key=API_KEY)
Path(OUTPUT_FOLDER).mkdir(exist_ok=True)
Path(INPUT_FOLDER).mkdir(exist_ok=True)

# ===== SYSTEM PROMPT =====
SYSTEM_PROMPT = """
You are a text analysis expert. Analyze the user's text and output JSON in this exact format:

{
    "sentiment": "positive" or "neutral" or "negative",
    "score": 0-100 (0 = most negative, 100 = most positive),
    "key_phrases": ["2-3 most important phrases"],
    "summary": "One sentence summary (max 100 characters)"
}
"""

# ===== FUNCTION: Analyze single text file =====
def analyze_file(file_path: Path) -> dict:
    """Read txt file, call OpenAI API, return JSON result"""
    
    # Read text from file
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    if not text.strip():
        return {"error": "File is empty", "file": file_path.name}
    
    # Call OpenAI API
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Cheap and fast
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text[:8000]}  # Limit length
            ],
            response_format={"type": "json_object"},  # Force JSON output
            temperature=0.3  # Lower = more consistent
        )
        
        # Parse and return JSON
        result = json.loads(response.choices[0].message.content)
        result["_source_file"] = file_path.name  # Add metadata
        return result
        
    except Exception as e:
        return {"error": str(e), "file": file_path.name}

# ===== MAIN: Batch process all files =====
def main():
    """Loop through all .txt files in input folder"""
    
    # Get all txt files
    txt_files = list(Path(INPUT_FOLDER).glob("*.txt"))
    
    if not txt_files:
        print(f"No .txt files found in '{INPUT_FOLDER}' folder")
        print(f"Please add some .txt files and run again")
        return
    
    print(f"Found {len(txt_files)} file(s)")
    print("-" * 40)
    
    # Process each file
    for file_path in txt_files:
        print(f"Analyzing: {file_path.name}")
        result = analyze_file(file_path)
        
        # Save result to JSON file
        output_file = Path(OUTPUT_FOLDER) / f"{file_path.stem}_analysis.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"Saved: {output_file}")
        print("-" * 40)
    
    print("All done!")

# ===== RUN =====
if __name__ == "__main__":
    main()