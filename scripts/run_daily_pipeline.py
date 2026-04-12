import csv
import datetime
import os

# --- The CSV Exporter Solution ---
# This bypasses all Google Cloud permissions blocks.
# 1. Run this script.
# 2. It generates 'new_tools_to_upload.csv'.
# 3. Open your Google Sheet -> File -> Import -> Upload this file -> "Append to current sheet".

def scrape_tools_engine():
    """ 
    This is the core engine where you will later scrape the web or ping APIs (ProductHunt, GitHub) to find tools.
    For this test run, here are 3 highly-rated real AI tools.
    """
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    return [
        {
            "Name": "Claude 3.5",
            "Slug": "claude",
            "Short Description": "Extremely advanced LLM by Anthropic with massive context windows.",
            "Full Details": "Claude is a next-generation AI assistant built for work and trained to be safe, accurate, and secure. It offers best-in-class coding capabilities, document analysis, and conversational intelligence.",
            "Category": "Writing",
            "Pricing": "Freemium",
            "URL": "https://claude.ai",
            "Logo URL": "https://claude.ai/favicon.ico",
            "Tags": "LLM, Chatbot, Coding",
            "Features": "Artifacts UI, 200k Context Window, Vision Analysis",
            "Date Added": today
        },
        {
            "Name": "Suno AI",
            "Slug": "suno",
            "Short Description": "Generate complete, studio-quality songs with vocals from a text prompt.",
            "Full Details": "Suno is building a future where anyone can make great music. It takes a text description of a song—including genre and topic—and generates full two-minute tracks complete with hyper-realistic human vocals and instrumentation.",
            "Category": "Audio",
            "Pricing": "Freemium",
            "URL": "https://suno.com",
            "Logo URL": "https://suno.com/favicon.ico",
            "Tags": "Music Generation, Audio",
            "Features": "Vocal Generation, Custom Lyrics, Radio Quality",
            "Date Added": today
        },
        {
            "Name": "Cursor IDE",
            "Slug": "cursor",
            "Short Description": "The AI-first code editor designed to make you instantly more productive.",
            "Full Details": "Cursor is a fork of VS Code imbued with advanced AI capabilities. Features like 'Composer' allow multi-file code generation and editing, completely changing the paradigm of software development.",
            "Category": "Coding",
            "Pricing": "Freemium",
            "URL": "https://cursor.com",
            "Logo URL": "https://cursor.com/favicon.ico",
            "Tags": "Developer Tools, IDE",
            "Features": "Multi-file Editing, Codebase Indexing, Copilot",
            "Date Added": today
        }
    ]

if __name__ == "__main__":
    print(f"🚀 Starting AI Tool CSV Generator...")
    tools = scrape_tools_engine()
    
    # The exact columns from your Google Sheet
    fieldnames = [
        "Name", "Slug", "Short Description", "Category", 
        "Pricing", "URL", "Logo URL", "Date Added", 
        "Full Details", "Tags", "Features"
    ]
    
    output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "new_tools_to_upload.csv")
    
    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for tool in tools:
            # Ensure missing columns are filled with empty string
            row = {field: tool.get(field, "") for field in fieldnames}
            writer.writerow(row)
            
    print(f"✅ Success! Found {len(tools)} tools.")
    print(f"📁 Saved perfectly formatted CSV to: {output_file}")
    print("\n👉 NEXT STEP: Open Google Sheets > File > Import > Upload > Select 'new_tools_to_upload.csv' > Choose 'Append to current sheet'")
