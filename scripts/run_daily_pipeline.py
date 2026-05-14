"""
AI Kendra — Daily Auto-Scraper Pipeline v2
============================================
Runs daily via GitHub Actions. Sources:

1. CSV BACKLOG: scripts/backlog.csv — large file of tools not yet in DB.
2. GITHUB TRENDING: Multiple search queries for broader coverage.

Output: Updates data/tools.json with correctly formatted entries.
"""

import json, datetime, os, urllib.request, urllib.error, re, csv, random, time

# CONFIG
TOOLS_PER_DAY = 8
GITHUB_TOOLS_PER_DAY = 5
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_JSON_PATH = os.path.join(BASE_DIR, "..", "data", "tools.json")
BACKLOG_CSV = os.path.join(BASE_DIR, "backlog.csv")

VALID_CATEGORIES = [
    "Writing", "Image Generation", "Video Creation", "Audio & Voice",
    "Coding & Development", "Productivity", "Marketing", "Finance",
    "Automation", "Research"
]

def make_slug(name):
    slug = name.lower().strip()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug

def make_logo(url):
    domain = url.replace("https://", "").replace("http://", "").split("/")[0]
    return f"https://www.google.com/s2/favicons?domain={domain}&sz=128"

def today_str():
    return datetime.datetime.now().strftime("%m/%d/%Y")

# SOURCE 1: CSV BACKLOG
def get_backlog_tools(existing_slugs):
    """Read from backlog.csv, return tools not already in DB."""
    if not os.path.exists(BACKLOG_CSV):
        print("[Backlog] backlog.csv not found, skipping.")
        return []
    
    tools = []
    with open(BACKLOG_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = make_slug(row['name'])
            if slug in existing_slugs:
                continue
            tools.append({
                "name": row['name'],
                "slug": slug,
                "shortDescription": row['description'][:200],
                "category": row['category'] if row['category'] in VALID_CATEGORIES else "Productivity",
                "pricing": row.get('pricing', 'Freemium'),
                "url": row['url'],
                "logo": make_logo(row['url']),
                "dateAdded": today_str(),
                "featured": False
            })
    
    random.shuffle(tools)
    print(f"[Backlog] {len(tools)} tools remaining in CSV")
    return tools[:TOOLS_PER_DAY]

# SOURCE 2: GITHUB TRENDING (multiple queries)
def fetch_github_trending(existing_slugs):
    """Search GitHub with multiple queries for broader coverage."""
    queries = [
        "topic:ai+topic:tool+stars:>30",
        "topic:llm+stars:>50",
        "topic:machine-learning+topic:tool+stars:>30",
        "topic:generative-ai+stars:>20",
        "topic:chatgpt+stars:>20",
        "topic:stable-diffusion+stars:>20",
        "topic:ai-agent+stars:>15",
    ]
    
    days_back = 14
    date_cutoff = (datetime.datetime.now() - datetime.timedelta(days=days_back)).strftime("%Y-%m-%d")
    
    all_tools = []
    for q in queries:
        url = f"https://api.github.com/search/repositories?q={q}+created:>{date_cutoff}&sort=stars&order=desc&per_page=5"
        try:
            req = urllib.request.Request(url, headers={
                "Accept": "application/vnd.github.v3+json",
                "User-Agent": "AI-Kendra-Scraper"
            })
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())
        except Exception as e:
            print(f"[GitHub] Query failed: {e}")
            continue
        
        for repo in data.get("items", []):
            name = repo["name"].replace("-", " ").replace("_", " ").title()
            desc = repo.get("description", "") or ""
            if len(desc) < 20:
                continue
            slug = make_slug(name)
            if slug in existing_slugs:
                continue
            
            topics = [t.lower() for t in repo.get("topics", [])]
            category = "Coding & Development"
            cat_map = {
                "image": "Image Generation", "art": "Image Generation", "diffusion": "Image Generation",
                "video": "Video Creation", "audio": "Audio & Voice", "voice": "Audio & Voice",
                "writing": "Writing", "nlp": "Writing",
                "automation": "Automation", "workflow": "Automation",
                "finance": "Finance", "trading": "Finance",
                "marketing": "Marketing", "seo": "Marketing",
                "productivity": "Productivity",
                "research": "Research", "paper": "Research",
            }
            for topic in topics:
                for kw, cat in cat_map.items():
                    if kw in topic:
                        category = cat
                        break
            
            homepage = repo.get("homepage") or repo["html_url"]
            all_tools.append({
                "name": name,
                "slug": slug,
                "shortDescription": desc[:200].strip(),
                "category": category,
                "pricing": "Open Source",
                "url": homepage,
                "logo": make_logo(homepage),
                "dateAdded": today_str(),
                "featured": False
            })
            existing_slugs.add(slug)
        
        time.sleep(2)  # Rate limit courtesy
    
    # Deduplicate by slug
    seen = set()
    unique = []
    for t in all_tools:
        if t["slug"] not in seen:
            seen.add(t["slug"])
            unique.append(t)
    
    print(f"[GitHub] Found {len(unique)} new trending repos")
    return unique[:GITHUB_TOOLS_PER_DAY]


# MAIN
if __name__ == "__main__":
    print("=" * 50)
    print("AI Kendra — Daily Auto-Scraper v2")
    print("=" * 50)
    
    if os.path.exists(TOOLS_JSON_PATH):
        with open(TOOLS_JSON_PATH, 'r', encoding='utf-8') as f:
            existing_tools = json.load(f)
    else:
        existing_tools = []
    
    existing_slugs = {t.get("slug") for t in existing_tools if "slug" in t}
    print(f"Database: {len(existing_tools)} tools\n")
    
    # Source 1: CSV Backlog
    print("[Backlog] Scanning...")
    backlog_tools = get_backlog_tools(existing_slugs)
    
    # Source 2: GitHub Trending
    print("\n[GitHub] Searching...")
    github_tools = fetch_github_trending(existing_slugs)
    
    # Merge
    all_new = backlog_tools + github_tools
    added = 0
    for tool in all_new:
        if tool["slug"] not in existing_slugs:
            existing_tools.insert(0, tool)
            existing_slugs.add(tool["slug"])
            added += 1
            print(f"  + {tool['name']} [{tool['category']}]")
    
    if added > 0:
        with open(TOOLS_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(existing_tools, f, indent=2, ensure_ascii=False)
        print(f"\nAdded {added} new tools!")
    else:
        print("\nNo new tools found today.")
    
    print(f"Total: {len(existing_tools)}")
    print("=" * 50)
