import json
import datetime
import os

# --- Phase 2: Native JSON Scraper Engine ---
# This script natively injects tools into data/tools.json for the Git-based setup.

def scrape_tools_engine():
    """ 
    This is the core engine where you will later scrape the web or ping APIs (ProductHunt, GitHub) to find tools.
    For this test run, here are highly-rated real AI tools to verify the automatic build pipeline works.
    You will replace this array later with your scraping logic!
    """
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    return [
        {
            "Name": "Midjourney V6",
            "Slug": "midjourney-v6",
            "Short Description": "Generate hyper-realistic AI art and images from text prompts via Discord.",
            "Full Details": "Midjourney is an independent research lab exploring new mediums of thought and expanding the imaginative powers of the human species. V6 brings incredibly realistic photorealistic generation, massive text-rendering improvements, and granular prompting control.",
            "Category": "Design",
            "Pricing": "Paid",
            "URL": "https://midjourney.com",
            "Logo URL": "https://midjourney.com/favicon.ico",
            "Tags": "Image Generation, Art, Discord",
            "Features": "Text-to-Image, Photorealism, Style Tuning",
            "Date Added": today
        },
        {
            "Name": "Perplexity AI",
            "Slug": "perplexity",
            "Short Description": "The AI search engine that gives you citations and instant answers.",
            "Full Details": "Perplexity is a conversational search engine that gives you instant, referenced answers to any question. Unlike traditional search engines that give you a list of links, Perplexity reads the links and writes a comprehensive answer with inline citations.",
            "Category": "Search",
            "Pricing": "Freemium",
            "URL": "https://perplexity.ai",
            "Logo URL": "https://perplexity.ai/favicon.ico",
            "Tags": "Search Engine, Research, Citations",
            "Features": "Copilot Search, File Upload, Inline Citations",
            "Date Added": today
        }
    ]

if __name__ == "__main__":
    print("🚀 Starting AI Tool Auto-Scraper...")
    tools_to_add = scrape_tools_engine()
    
    tools_json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "tools.json")
    
    # Read existing tools
    if os.path.exists(tools_json_path):
        with open(tools_json_path, 'r', encoding='utf-8') as f:
            try:
                existing_tools = json.load(f)
            except:
                existing_tools = []
    else:
        existing_tools = []
        
    print(f"📖 Loaded {len(existing_tools)} existing tools from database.")
    
    # Check for duplicates using the Slug
    existing_slugs = {t.get("Slug") for t in existing_tools if "Slug" in t}
    added_count = 0
    
    for new_tool in tools_to_add:
        if new_tool["Slug"] not in existing_slugs:
            # We insert at the top so newest tools appear first!
            existing_tools.insert(0, new_tool)
            existing_slugs.add(new_tool["Slug"])
            added_count += 1
            print(f"➕ Added completely new tool: {new_tool['Name']}")
        else:
            print(f"⏭️  Skipped duplicate tool: {new_tool['Name']}")
            
    # Write back to tools.json
    if added_count > 0:
        with open(tools_json_path, 'w', encoding='utf-8') as f:
            json.dump(existing_tools, f, indent=2, ensure_ascii=False)
        print(f"\n✅ Success! Instantly injected {added_count} new tools directly into GitHub Repository!")
    else:
        print("\n✅ Run complete. No entirely new tools found today.")
