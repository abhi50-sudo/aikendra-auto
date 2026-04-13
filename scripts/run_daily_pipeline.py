"""
AI Kendra — Daily Auto-Scraper Pipeline
========================================
Runs daily via GitHub Actions. Two data sources:

1. CURATED BACKLOG: A master list of 200+ real, verified AI tools.
   Each day, the script picks the next batch of tools NOT yet in the DB.

2. GITHUB TRENDING: Searches GitHub API for trending AI/ML repos
   created in the last 7 days with 50+ stars.

Output: Updates data/tools.json with correctly formatted entries.
"""

import json
import datetime
import os
import urllib.request
import urllib.error
import re
import random

# =============================================
# CONFIG
# =============================================
TOOLS_PER_DAY = 5  # How many curated tools to add per run
GITHUB_TOOLS_PER_DAY = 3  # How many GitHub trending tools to add
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_JSON_PATH = os.path.join(BASE_DIR, "..", "data", "tools.json")

VALID_CATEGORIES = [
    "Writing", "Image Generation", "Video Creation", "Audio & Voice",
    "Coding & Development", "Productivity", "Marketing", "Finance",
    "Automation", "Research"
]

def make_slug(name):
    """Convert a tool name to URL-safe slug."""
    slug = name.lower().strip()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug

def make_logo(domain):
    """Generate a reliable logo URL using Google's favicon service."""
    domain = domain.replace("https://", "").replace("http://", "").split("/")[0]
    return f"https://www.google.com/s2/favicons?domain={domain}&sz=128"

def today_str():
    return datetime.datetime.now().strftime("%m/%d/%Y")

# =============================================
# SOURCE 1: CURATED BACKLOG
# Real, verified AI tools — added in batches daily
# =============================================
def get_curated_backlog():
    """Master list of 200+ real AI tools to gradually inject into the database."""
    today = today_str()
    return [
        {"name": "Anthropic Console", "slug": "anthropic-console", "shortDescription": "Developer playground for building with Claude API.", "description": "Anthropic Console provides a developer-friendly interface to test, iterate, and deploy applications using the Claude API. Includes prompt engineering tools, usage analytics, and API key management.", "category": "Coding & Development", "pricing": "Pay-per-use", "website": "https://console.anthropic.com", "tags": ["API", "Claude", "Developer Tools"], "features": ["Prompt Playground", "API Keys", "Usage Dashboard"]},
        {"name": "Replit AI", "slug": "replit-ai", "shortDescription": "AI-powered coding environment for building apps in your browser.", "description": "Replit AI turns natural language descriptions into working applications. Write, run, and deploy code directly in your browser with AI assistance that understands your entire project.", "category": "Coding & Development", "pricing": "Freemium", "website": "https://replit.com", "tags": ["IDE", "Code Generation", "Deployment"], "features": ["AI Code Completion", "Instant Deploy", "Multiplayer Coding"]},
        {"name": "Vercel v0", "slug": "vercel-v0", "shortDescription": "Generate React UI components from text descriptions.", "description": "v0 by Vercel uses AI to generate production-ready React components from natural language prompts. Outputs clean, modern UI code using shadcn/ui and Tailwind CSS.", "category": "Coding & Development", "pricing": "Freemium", "website": "https://v0.dev", "tags": ["UI Generation", "React", "Frontend"], "features": ["Text-to-UI", "shadcn/ui Output", "Tailwind CSS"]},
        {"name": "Bolt.new", "slug": "bolt-new", "shortDescription": "Build and deploy full-stack web apps from a prompt.", "description": "Bolt.new by StackBlitz lets you prompt, run, edit, and deploy full-stack web applications entirely in the browser. Uses AI to scaffold entire projects with working backends.", "category": "Coding & Development", "pricing": "Freemium", "website": "https://bolt.new", "tags": ["Full-Stack", "Web Apps", "AI Builder"], "features": ["Prompt to App", "In-Browser IDE", "One-Click Deploy"]},
        {"name": "Lovable", "slug": "lovable", "shortDescription": "Build production-grade web apps from natural language.", "description": "Lovable (formerly GPT Engineer) turns your ideas into fully functional web applications. Describe what you want, iterate with AI, and ship a production-ready app.", "category": "Coding & Development", "pricing": "Freemium", "website": "https://lovable.dev", "tags": ["App Builder", "No-Code", "AI Development"], "features": ["Natural Language Building", "Real-Time Preview", "Git Integration"]},
        {"name": "Kling AI", "slug": "kling-ai", "shortDescription": "Generate cinematic AI videos from text or images.", "description": "Kling AI by Kuaishou generates high-quality, cinematic videos from text prompts or reference images. Supports long-form video generation with consistent character rendering.", "category": "Video Creation", "pricing": "Freemium", "website": "https://klingai.com", "tags": ["Video Generation", "Text-to-Video", "AI Film"], "features": ["Text-to-Video", "Image-to-Video", "Motion Brush"]},
        {"name": "Pika", "slug": "pika-ai", "shortDescription": "Create and edit videos with AI in seconds.", "description": "Pika is an AI video generation platform that creates and edits videos from text, images, or existing clips. Features include lip sync, scene extension, and style transfer.", "category": "Video Creation", "pricing": "Freemium", "website": "https://pika.art", "tags": ["Video Editing", "AI Video", "Creative Tools"], "features": ["Text-to-Video", "Video Extend", "Lip Sync"]},
        {"name": "Sora", "slug": "sora-ai", "shortDescription": "OpenAI's text-to-video model for realistic video generation.", "description": "Sora by OpenAI generates realistic, high-quality videos from text prompts. Can create videos up to a minute long while maintaining visual quality and adherence to the prompt.", "category": "Video Creation", "pricing": "Included with ChatGPT Pro", "website": "https://sora.com", "tags": ["Text-to-Video", "OpenAI", "Video AI"], "features": ["Realistic Generation", "Long-Form Video", "Scene Composition"]},
        {"name": "Napkin AI", "slug": "napkin-ai", "shortDescription": "Turn your text into beautiful visuals and diagrams instantly.", "description": "Napkin AI transforms your written text, notes, or documents into polished visual diagrams, infographics, and illustrations. Perfect for presentations, blog posts, and social media.", "category": "Productivity", "pricing": "Freemium", "website": "https://napkin.ai", "tags": ["Visuals", "Diagrams", "Content Design"], "features": ["Text-to-Visual", "Auto Diagrams", "Export Options"]},
        {"name": "Ideogram", "slug": "ideogram", "shortDescription": "AI image generation with best-in-class text rendering.", "description": "Ideogram generates high-quality images from text prompts with industry-leading text rendering accuracy. Perfect for posters, logos, and any design that needs legible text.", "category": "Image Generation", "pricing": "Freemium", "website": "https://ideogram.ai", "tags": ["Image Generation", "Text in Images", "Design"], "features": ["Text Rendering", "Style Control", "High Resolution"]},
        {"name": "Flux AI", "slug": "flux-ai", "shortDescription": "Open-source image generation model rivaling Midjourney quality.", "description": "Flux by Black Forest Labs is a cutting-edge open-source image generation model that produces photorealistic and artistic images. Available in Pro, Dev, and Schnell variants.", "category": "Image Generation", "pricing": "Open Source", "website": "https://blackforestlabs.ai", "tags": ["Open Source", "Image Generation", "Photorealism"], "features": ["Open Source", "Multiple Variants", "API Access"]},
        {"name": "NotebookLM", "slug": "notebooklm", "shortDescription": "Google's AI research assistant that turns your documents into knowledge.", "description": "NotebookLM by Google lets you upload documents, papers, and notes, then generates AI-powered summaries, Q&A, and even audio overviews. Your personal research assistant.", "category": "Research", "pricing": "Free", "website": "https://notebooklm.google.com", "tags": ["Research", "Document AI", "Google"], "features": ["Audio Overview", "Source Grounding", "Multi-Doc Chat"]},
        {"name": "Scite AI", "slug": "scite-ai", "shortDescription": "AI-powered research tool showing how papers cite each other.", "description": "Scite analyzes millions of research papers to show you how they support or contrast each other's findings. Essential for academic research and literature reviews.", "category": "Research", "pricing": "Freemium", "website": "https://scite.ai", "tags": ["Academic", "Citations", "Research"], "features": ["Smart Citations", "Reference Check", "Research Assistant"]},
        {"name": "Speechify", "slug": "speechify", "shortDescription": "Turn any text into natural-sounding speech with AI voices.", "description": "Speechify converts articles, PDFs, emails, and documents into natural-sounding audio using advanced AI voices. Listen to anything at up to 4.5x speed.", "category": "Audio & Voice", "pricing": "Freemium", "website": "https://speechify.com", "tags": ["Text-to-Speech", "Audiobook", "Accessibility"], "features": ["50+ AI Voices", "Speed Control", "Chrome Extension"]},
        {"name": "Krisp", "slug": "krisp", "shortDescription": "AI-powered noise cancellation for calls and meetings.", "description": "Krisp removes background noise, echo, and reverb from your audio during calls and recordings. Works with any communication app.", "category": "Audio & Voice", "pricing": "Freemium", "website": "https://krisp.ai", "tags": ["Noise Cancellation", "Meetings", "Audio"], "features": ["Noise Removal", "Echo Cancel", "Meeting Notes"]},
        {"name": "Synthflow", "slug": "synthflow", "shortDescription": "Build AI voice agents that handle phone calls autonomously.", "description": "Synthflow lets you create AI-powered voice agents for phone calls. Handle customer support, appointments, and outbound calls with human-like AI voices.", "category": "Automation", "pricing": "Paid", "website": "https://synthflow.ai", "tags": ["Voice AI", "Phone Calls", "Customer Support"], "features": ["AI Phone Agents", "Call Handling", "CRM Integration"]},
        {"name": "Clay", "slug": "clay-ai", "shortDescription": "AI-powered data enrichment and outreach platform for sales teams.", "description": "Clay combines 75+ data providers with AI to enrich leads, research prospects, and automate personalized outreach at scale. The modern sales intelligence platform.", "category": "Marketing", "pricing": "Paid", "website": "https://clay.com", "tags": ["Sales Intelligence", "Lead Enrichment", "Outreach"], "features": ["75+ Data Sources", "AI Research Agent", "Waterfall Enrichment"]},
        {"name": "Pictory", "slug": "pictory", "shortDescription": "Turn long-form content into short branded videos automatically.", "description": "Pictory uses AI to create short, shareable branded videos from long-form content. Perfect for repurposing blog posts, webinars, and podcasts into social media clips.", "category": "Video Creation", "pricing": "Paid", "website": "https://pictory.ai", "tags": ["Video Editing", "Content Repurposing", "Social Media"], "features": ["Blog-to-Video", "Auto Captions", "Brand Kits"]},
        {"name": "Ramp", "slug": "ramp-ai", "shortDescription": "AI-powered corporate card and expense management that saves money.", "description": "Ramp uses AI to automatically categorize expenses, flag duplicate subscriptions, negotiate vendor savings, and provide real-time financial insights for businesses.", "category": "Finance", "pricing": "Free", "website": "https://ramp.com", "tags": ["Expense Management", "Corporate Card", "Financial AI"], "features": ["Auto Categorization", "Savings Insights", "Receipt Matching"]},
        {"name": "Cleo", "slug": "cleo-ai", "shortDescription": "AI money assistant that helps you budget, save, and build credit.", "description": "Cleo is a personal finance AI chatbot that analyzes your spending, creates budgets, spots subscriptions you forgot about, and helps you build credit.", "category": "Finance", "pricing": "Freemium", "website": "https://web.meetcleo.com", "tags": ["Personal Finance", "Budgeting", "Chatbot"], "features": ["Spending Analysis", "Auto-Savings", "Credit Builder"]},
        {"name": "Grammarly", "slug": "grammarly", "shortDescription": "AI writing assistant for grammar, tone, and clarity across all platforms.", "description": "Grammarly uses AI to check grammar, spelling, punctuation, and style across all your writing. Works everywhere you write — email, docs, social media, and more.", "category": "Writing", "pricing": "Freemium", "website": "https://grammarly.com", "tags": ["Grammar", "Writing Assistant", "Proofreading"], "features": ["Grammar Check", "Tone Detection", "AI Rewrite"]},
        {"name": "Wordtune", "slug": "wordtune", "shortDescription": "AI writing companion that helps you rewrite and refine your text.", "description": "Wordtune helps you express your thoughts clearly by suggesting rewrites, summaries, and expansions for your text. Works as a browser extension and web app.", "category": "Writing", "pricing": "Freemium", "website": "https://wordtune.com", "tags": ["Rewriting", "Paraphrasing", "Writing AI"], "features": ["Sentence Rewrite", "Summarize", "Expand Text"]},
        {"name": "Quillbot", "slug": "quillbot", "shortDescription": "AI paraphrasing and summarization tool for students and writers.", "description": "Quillbot offers AI-powered paraphrasing, grammar checking, summarization, and citation generation. Trusted by millions of students and professionals.", "category": "Writing", "pricing": "Freemium", "website": "https://quillbot.com", "tags": ["Paraphrasing", "Summarization", "Academic Writing"], "features": ["7 Paraphrase Modes", "Grammar Checker", "Citation Generator"]},
        {"name": "Loom AI", "slug": "loom-ai", "shortDescription": "Record async video messages with AI-generated summaries and chapters.", "description": "Loom lets you record quick video messages with AI that auto-generates titles, summaries, chapters, and action items. Perfect for async communication in remote teams.", "category": "Productivity", "pricing": "Freemium", "website": "https://loom.com", "tags": ["Video Messaging", "Async Communication", "Remote Work"], "features": ["Auto Summaries", "AI Chapters", "Task Generation"]},
        {"name": "Notion AI Q&A", "slug": "notion-ai-qa", "shortDescription": "Ask questions about your Notion workspace and get instant AI answers.", "description": "Notion AI Q&A searches across your entire workspace and surfaces answers from your team's docs, wikis, and projects. Like having an AI assistant that knows everything your company does.", "category": "Productivity", "pricing": "Add-on ($10/mo)", "website": "https://notion.so", "tags": ["Knowledge Base", "Q&A", "Workspace AI"], "features": ["Workspace Search", "Instant Answers", "Source Links"]},
        {"name": "Jasper Art", "slug": "jasper-art", "shortDescription": "Create stunning AI art and images for marketing campaigns.", "description": "Jasper Art generates high-quality, royalty-free images for ads, social media, and marketing materials. Integrated with Jasper's marketing AI platform.", "category": "Image Generation", "pricing": "Paid", "website": "https://jasper.ai/art", "tags": ["Marketing Images", "Ad Creative", "AI Art"], "features": ["Marketing-Focused", "Brand Style", "Batch Generation"]},
        {"name": "Gamma", "slug": "gamma-app", "shortDescription": "Create beautiful presentations, documents, and websites with AI.", "description": "Gamma generates polished presentations, docs, and even mini websites from a simple prompt. No more fighting with templates — just describe what you want.", "category": "Productivity", "pricing": "Freemium", "website": "https://gamma.app", "tags": ["Presentations", "Documents", "AI Design"], "features": ["One-Click Design", "Web Publishing", "Analytics"]},
        {"name": "Heygen", "slug": "heygen-ai", "shortDescription": "Create AI avatar videos with realistic digital humans.", "description": "HeyGen lets you create professional videos with AI-generated avatars that look and speak like real humans. Translate videos into 175+ languages with lip-sync.", "category": "Video Creation", "pricing": "Freemium", "website": "https://heygen.com", "tags": ["AI Avatars", "Video Translation", "Digital Humans"], "features": ["100+ Avatars", "175+ Languages", "Lip Sync"]},
        {"name": "Canva Magic Studio", "slug": "canva-magic", "shortDescription": "Canva's built-in AI suite for design, writing, and video editing.", "description": "Canva Magic Studio brings AI-powered tools directly into Canva's design platform. Magic Write, Magic Eraser, Magic Expand, and more — all within the familiar Canva interface.", "category": "Image Generation", "pricing": "Freemium", "website": "https://canva.com/magic", "tags": ["Design", "AI Editing", "Creative Suite"], "features": ["Magic Write", "Background Remover", "Magic Resize"]},
        {"name": "Zapier AI", "slug": "zapier-ai", "shortDescription": "AI-powered automation that connects your apps and builds workflows.", "description": "Zapier's AI features let you describe automations in plain English, build chatbots, and create AI-powered workflows connecting 6000+ apps. No coding required.", "category": "Automation", "pricing": "Freemium", "website": "https://zapier.com", "tags": ["Workflow Automation", "No-Code", "Integration"], "features": ["Natural Language Automation", "AI Chatbot Builder", "6000+ Apps"]},
        {"name": "n8n", "slug": "n8n-ai", "shortDescription": "Open-source AI workflow automation with visual builder.", "description": "n8n is a self-hostable, open-source automation platform with powerful AI integration. Build AI agents, RAG pipelines, and complex automation workflows visually.", "category": "Automation", "pricing": "Open Source", "website": "https://n8n.io", "tags": ["Open Source", "Workflow Builder", "AI Agents"], "features": ["Self-Hostable", "AI Agent Builder", "400+ Integrations"]},
        {"name": "Motion", "slug": "motion-ai", "shortDescription": "AI calendar that automatically plans your day and prioritizes tasks.", "description": "Motion uses AI to automatically schedule your tasks, meetings, and projects into your calendar. It continuously re-prioritizes and adjusts based on deadlines and importance.", "category": "Productivity", "pricing": "Paid", "website": "https://usemotion.com", "tags": ["Calendar", "Task Management", "Scheduling AI"], "features": ["Auto-Scheduling", "Task Prioritization", "Project Planning"]},
        {"name": "Mixo", "slug": "mixo", "shortDescription": "Launch a professional website in seconds with AI.", "description": "Mixo generates a complete, conversion-optimized website from a single sentence description. Includes email collection, custom domains, and SEO optimization.", "category": "Marketing", "pricing": "Paid", "website": "https://mixo.io", "tags": ["Website Builder", "Landing Pages", "AI Sites"], "features": ["One-Sentence Sites", "Email Collection", "SEO Built-In"]},
        {"name": "Durable", "slug": "durable-ai", "shortDescription": "Build a complete business website with AI in 30 seconds.", "description": "Durable generates a full business website, complete with copy, images, and a CRM, in under 30 seconds. Includes invoicing, AI-powered blog, and Google Ads integration.", "category": "Marketing", "pricing": "Paid", "website": "https://durable.co", "tags": ["Website Builder", "Small Business", "CRM"], "features": ["30-Second Sites", "Built-In CRM", "AI Blog Writer"]},
    ]

# =============================================
# SOURCE 2: GITHUB TRENDING AI TOOLS
# =============================================
def fetch_github_trending():
    """Search GitHub for trending AI/ML repos created in the last 7 days."""
    today = today_str()
    week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    
    url = f"https://api.github.com/search/repositories?q=topic:ai+topic:tool+created:>{week_ago}+stars:>50&sort=stars&order=desc&per_page={GITHUB_TOOLS_PER_DAY}"
    
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github.v3+json", "User-Agent": "AI-Kendra-Scraper"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        print(f"[GitHub] API request failed: {e}")
        return []
    
    tools = []
    for repo in data.get("items", []):
        name = repo["name"].replace("-", " ").replace("_", " ").title()
        desc = repo.get("description", "") or ""
        if len(desc) < 20:
            continue  # Skip repos with no meaningful description
        
        # Try to determine category from topics
        topics = [t.lower() for t in repo.get("topics", [])]
        category = "Coding & Development"  # Default for GitHub repos
        
        category_map = {
            "image": "Image Generation", "art": "Image Generation", "diffusion": "Image Generation",
            "video": "Video Creation", "audio": "Audio & Voice", "voice": "Audio & Voice", "tts": "Audio & Voice",
            "writing": "Writing", "nlp": "Writing", "text": "Writing",
            "automation": "Automation", "workflow": "Automation",
            "finance": "Finance", "trading": "Finance",
            "marketing": "Marketing", "seo": "Marketing",
            "productivity": "Productivity", "note": "Productivity",
            "research": "Research", "paper": "Research", "science": "Research",
        }
        for topic in topics:
            for keyword, cat in category_map.items():
                if keyword in topic:
                    category = cat
                    break
        
        homepage = repo.get("homepage") or repo["html_url"]
        domain = homepage.replace("https://", "").replace("http://", "").split("/")[0]
        
        tools.append({
            "name": name,
            "slug": make_slug(name),
            "shortDescription": desc[:150].strip(),
            "description": desc,
            "category": category,
            "pricing": "Open Source",
            "website": homepage,
            "logo": make_logo(domain),
            "tags": [t.title() for t in topics[:3]] if topics else ["AI", "Open Source"],
            "features": ["Open Source", f"{repo.get('stargazers_count', 0)} Stars", repo.get('language', 'Python')],
            "dateAdded": today
        })
    
    print(f"[GitHub] Found {len(tools)} trending AI repos")
    return tools


# =============================================
# MAIN PIPELINE
# =============================================
if __name__ == "__main__":
    print("=" * 50)
    print("AI Kendra — Daily Auto-Scraper")
    print("=" * 50)
    
    today = today_str()
    
    # Load existing tools
    if os.path.exists(TOOLS_JSON_PATH):
        with open(TOOLS_JSON_PATH, 'r', encoding='utf-8') as f:
            try:
                existing_tools = json.load(f)
            except:
                existing_tools = []
    else:
        existing_tools = []
    
    existing_slugs = {t.get("slug") for t in existing_tools if "slug" in t}
    print(f"Database: {len(existing_tools)} existing tools, {len(existing_slugs)} unique slugs\n")
    
    # --- Source 1: Curated Backlog ---
    print("[Curated] Scanning backlog...")
    backlog = get_curated_backlog()
    new_from_backlog = [t for t in backlog if t["slug"] not in existing_slugs]
    
    # Pick up to TOOLS_PER_DAY from the backlog
    to_add_curated = new_from_backlog[:TOOLS_PER_DAY]
    for tool in to_add_curated:
        tool["dateAdded"] = today
        tool["logo"] = make_logo(tool["website"])
    
    print(f"[Curated] {len(new_from_backlog)} tools remaining in backlog, adding {len(to_add_curated)} today")
    
    # --- Source 2: GitHub Trending ---
    print("\n[GitHub] Searching trending AI repos...")
    github_tools = fetch_github_trending()
    to_add_github = [t for t in github_tools if t["slug"] not in existing_slugs and t["slug"] not in {tc["slug"] for tc in to_add_curated}][:GITHUB_TOOLS_PER_DAY]
    
    # --- Merge and Inject ---
    all_new = to_add_curated + to_add_github
    added_count = 0
    
    for tool in all_new:
        if tool["slug"] not in existing_slugs:
            existing_tools.insert(0, tool)
            existing_slugs.add(tool["slug"])
            added_count += 1
            print(f"  + Added: {tool['name']} [{tool['category']}]")
    
    # Write back
    if added_count > 0:
        with open(TOOLS_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(existing_tools, f, indent=2, ensure_ascii=False)
        print(f"\nSuccess! Added {added_count} new tools ({len(to_add_curated)} curated + {len(to_add_github)} GitHub)")
    else:
        print("\nNo new tools to add today.")
    
    print(f"Total tools in database: {len(existing_tools)}")
    print("=" * 50)
