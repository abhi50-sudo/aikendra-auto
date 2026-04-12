import csv
import datetime
import os
import re

today = datetime.datetime.now().strftime("%Y-%m-%d")

# Simple dataset: Name, Category, Pricing, URL, Short Desc, Tags
raw_tools = [
    ("ChatGPT", "Productivity", "Freemium", "https://chatgpt.com", "Advanced conversational AI by OpenAI.", "LLM, Chatbot, Assistant"),
    ("Midjourney", "Image Generation", "Paid", "https://midjourney.com", "High-quality AI image generation from text prompts.", "Art, Design, Text-to-Image"),
    ("Perplexity", "Research", "Freemium", "https://perplexity.ai", "AI search engine that provides cited answers.", "Search, Research, Web"),
    ("Notion AI", "Productivity", "Paid", "https://notion.so", "AI integrated workspace for notes and docs.", "Notes, Writing, Workspace"),
    ("Gamma", "Productivity", "Freemium", "https://gamma.app", "Create beautiful presentations and documents with AI.", "Presentations, Slides, Design"),
    ("Runway", "Video Creation", "Freemium", "https://runwayml.com", "Advanced AI video generation and editing tools.", "Video, Generation, Editor"),
    ("ElevenLabs", "Audio & Voice", "Freemium", "https://elevenlabs.io", "Ultra-realistic text-to-speech voice generation.", "Voice, TTS, Audio"),
    ("Phind", "Coding & Development", "Free", "https://phind.com", "AI search engine tailored specifically for developers.", "Coding, Search, Developer"),
    ("V0 by Vercel", "Coding & Development", "Freemium", "https://v0.dev", "Generative UI system by Vercel.", "UI, React, Frontend"),
    ("HeyGen", "Video Creation", "Freemium", "https://heygen.com", "AI video generator with photorealistic avatars.", "Avatars, Video, Presentations"),
    ("Synthesia", "Video Creation", "Paid", "https://synthesia.io", "Create videos from text with AI avatars.", "Video, Enterprise, TTS"),
    ("Copy.ai", "Marketing", "Freemium", "https://copy.ai", "AI copywriter for marketing and sales teams.", "Writing, Marketing, Copy"),
    ("Jasper", "Marketing", "Paid", "https://jasper.ai", "Enterprise-grade AI marketing copilot.", "Writing, Brand, Marketing"),
    ("DeepL", "Writing", "Freemium", "https://deepl.com", "The world's most accurate AI translator.", "Translation, Languages, Writing"),
    ("Poe", "Productivity", "Freemium", "https://poe.com", "Access multiple top-tier AI models in one app.", "Chatbot, Multi-model, Assistant"),
    ("Gemini", "Productivity", "Freemium", "https://gemini.google.com", "Google's direct competitor to ChatGPT.", "Google, LLM, Assistant"),
    ("Github Copilot", "Coding & Development", "Paid", "https://github.com/features/copilot", "Your AI pair programmer inside your IDE.", "Coding, Autocomplete, Developer"),
    ("Devin", "Coding & Development", "Paid", "https://cognition.ai/devin", "The first fully autonomous AI software engineer.", "Autonomous, Agent, Coding"),
    ("Replicate", "Coding & Development", "Paid", "https://replicate.com", "Run open-source AI models with an API.", "API, Open Source, Hosting"),
    ("Hugging Face", "Coding & Development", "Free", "https://huggingface.co", "The platform for machine learning community.", "Models, Datasets, ML"),
    ("Framer", "Productivity", "Freemium", "https://framer.com", "Design and publish stunning websites with AI.", "Web Design, No-Code, Editor"),
    ("Leonardo AI", "Image Generation", "Freemium", "https://leonardo.ai", "Produce stunning game assets and artwork.", "Gaming, Art, Generation"),
    ("Krea AI", "Image Generation", "Freemium", "https://krea.ai", "Real-time AI image generation and enhancement.", "Real-time, Upscaling, Design"),
    ("Stable Diffusion", "Image Generation", "Free", "https://stability.ai", "Open-source image generation model.", "Open Source, Art, Generator"),
    ("Magnific AI", "Image Generation", "Paid", "https://magnific.ai", "The most advanced AI image upscaler and enhancer.", "Upscaling, Enhancement, Resolution"),
    ("Luma Dream Machine", "Video Creation", "Freemium", "https://lumalabs.ai/dream-machine", "High quality AI video generation model.", "Video, Generative, 3D"),
    ("Suno", "Audio & Voice", "Freemium", "https://suno.com", "Create full songs with vocals from a prompt.", "Music, Generation, Vocals"),
    ("Udio", "Audio & Voice", "Freemium", "https://udio.com", "AI music generator for high-fidelity tracks.", "Music, Audio, Tracks"),
    ("Murf AI", "Audio & Voice", "Freemium", "https://murf.ai", "Versatile text to speech software with multiple voices.", "TTS, Voiceover, Audio"),
    ("Descript", "Audio & Voice", "Freemium", "https://descript.com", "Edit audio and video by editing text.", "Podcast, Editing, Transcription"),
    ("Otter.ai", "Productivity", "Freemium", "https://otter.ai", "AI meeting assistant that records and transcribes.", "Meetings, Notes, Transcription"),
    ("Fireflies.ai", "Productivity", "Freemium", "https://fireflies.ai", "Automate your meeting notes and transcripts.", "Meetings, Search, Voice"),
    ("Zapier Central", "Automation", "Freemium", "https://zapier.com/central", "AI bots that automate tasks across your apps.", "Automation, Workflows, Bots"),
    ("Make", "Automation", "Freemium", "https://make.com", "Visual platform to design and automate workflows.", "No-Code, Workflows, Integration"),
    ("Beautiful.ai", "Productivity", "Paid", "https://beautiful.ai", "Presentation maker that designs for you.", "Slides, Pitch, Design"),
    ("Tome", "Productivity", "Freemium", "https://tome.app", "AI-powered storytelling and presentation format.", "Storytelling, Decks, Layouts"),
    ("Writesonic", "Writing", "Freemium", "https://writesonic.com", "AI writer, copywriter and paragraph creator.", "SEO, Blogs, Ads"),
    ("Rytr", "Writing", "Freemium", "https://rytr.me", "Fast, responsive AI writing assistant.", "Copy, Emails, Content"),
    ("GrammarlyGO", "Writing", "Freemium", "https://grammarly.com", "AI communication assistance everywhere you type.", "Grammar, Tone, Editing"),
    ("Cursor", "Coding & Development", "Freemium", "https://cursor.com", "AI-first code editor with powerful Composer.", "IDE, Editing, AI"),
    ("Claude", "Research", "Freemium", "https://claude.ai", "Anthropic's LLM built for large context windows.", "Analysis, Safe, Context"),
    ("Mistral", "Coding & Development", "Freemium", "https://mistral.ai", "Open-weight foundational models for developers.", "Open Source, Models, Fast"),
    ("Cohere", "Automation", "Paid", "https://cohere.com", "Enterprise AI platform for search and generation.", "Enterprise, NLP, API"),
    ("Glean", "Productivity", "Paid", "https://glean.com", "AI-powered enterprise search and knowledge.", "Enterprise, Intranet, Search"),
    ("Harvey", "Research", "Paid", "https://harvey.ai", "Generative AI for elite law firms.", "Legal, Professional, Analysis"),
    ("Codeium", "Coding & Development", "Free", "https://codeium.com", "Free AI code completion and chat.", "Autocomplete, IDE, Free"),
    ("Tabnine", "Coding & Development", "Freemium", "https://tabnine.com", "Private and secure AI assistant for developers.", "Privacy, Enterprise, Autocomplete"),
    ("Liner", "Research", "Freemium", "https://getliner.com", "AI workspace for researchers and students.", "Highlighting, Summarization, Web"),
    ("Consensus", "Research", "Freemium", "https://consensus.app", "AI search engine for scientific research.", "Science, Papers, Citations"),
    ("Elicit", "Research", "Freemium", "https://elicit.com", "Analyze research papers at superhuman speed.", "Literature Review, Data, Academic"),
    ("ChatPDF", "Productivity", "Freemium", "https://chatpdf.com", "Chat with any PDF document seamlessly.", "PDF, Reading, Search"),
    ("SciSpace", "Research", "Freemium", "https://typeset.io", "Do hours of research in minutes.", "Papers, Complex, Formats"),
    ("Canva Magic Studio", "Image Generation", "Freemium", "https://canva.com", "All-in-one AI design tools within Canva.", "Graphic Design, Social Media, Suite"),
    ("Adobe Firefly", "Image Generation", "Freemium", "https://firefly.adobe.com", "Generative AI for creative workflows by Adobe.", "Commercial Safe, Photoshop, Vectors"),
    ("Opus Clip", "Video Creation", "Freemium", "https://opus.pro", "Turn long videos into viral shorts in one click.", "Shorts, Repurposing, Viral"),
    ("CapCut", "Video Creation", "Freemium", "https://capcut.com", "Free all-in-one video editor with AI features.", "Editing, TikTok, Captions"),
    ("Syllaby", "Marketing", "Freemium", "https://syllaby.io", "Find viral topics and generate video scripts.", "Social Media, Scripts, Strategy"),
    ("Brandmark", "Image Generation", "Paid", "https://brandmark.io", "Create professional logos with AI.", "Branding, Assets, Logos"),
    ("Looka", "Image Generation", "Paid", "https://looka.com", "Design your own beautiful brand using AI.", "Branding, Identity, Logo"),
    ("Eightify", "Productivity", "Freemium", "https://eightify.app", "YouTube video summaries using AI.", "YouTube, Summaries, Time-saving"),
    ("Miro Assist", "Productivity", "Freemium", "https://miro.com", "AI partner for innovation and brainstorming.", "Whiteboard, Mindmaps, Diagrams"),
    ("Whimsical AI", "Productivity", "Freemium", "https://whimsical.com", "Generate mind maps and wireframes instantly.", "Wireframes, Planning, Ideation"),
    ("Julius AI", "Research", "Freemium", "https://julius.ai", "Your AI data analyst. Chat with your data.", "Data Science, Spreadsheets, Charts"),
    ("Rose", "Finance", "Freemium", "https://rose.ai", "Cloud data platform to find and visualize data.", "Finance, Markets, Visualization"),
    ("FinChat", "Finance", "Freemium", "https://finchat.io", "ChatGPT for investing and financial data.", "Stocks, Earnings, Investing"),
    ("AlphaSense", "Finance", "Paid", "https://alpha-sense.com", "Market intelligence and search platform.", "Enterprise, Wall Street, Research"),
    ("Apollo", "Marketing", "Freemium", "https://apollo.io", "AI powered sales intelligence and engagement.", "Sales, Leads, Outreach"),
    ("Instantly", "Marketing", "Paid", "https://instantly.ai", "Scale cold email outreach with unlimited accounts.", "Email, Cold Outreach, B2B"),
    ("Reply.io", "Marketing", "Paid", "https://reply.io", "AI sales engagement platform.", "Multichannel, Sequences, Sales"),
    ("Taplio", "Marketing", "Paid", "https://taplio.com", "Grow your personal brand on LinkedIn with AI.", "LinkedIn, Scheduling, Growth"),
    ("TweetHunter", "Marketing", "Paid", "https://tweethunter.io", "Build and monetize your Twitter audience.", "Twitter/X, Ghostwriting, Analytics"),
    ("Superhuman", "Productivity", "Paid", "https://superhuman.com", "The fastest email experience ever made, now with AI.", "Email, Speed, Workflow"),
    ("Arc Search", "Productivity", "Free", "https://arc.net", "Browser that browses for you, summarizing pages.", "Mobile, Browser, Tabs"),
    ("Raycast", "Productivity", "Freemium", "https://raycast.com", "Blazingly fast, totally extendable launcher.", "Mac, Commands, AI Integration"),
    ("Mem", "Productivity", "Paid", "https://mem.ai", "The AI workspace that organizes itself.", "Notes, Self-organizing, Brain"),
    ("Taskade", "Automation", "Freemium", "https://taskade.com", "Build a team of AI agents for your workflows.", "Tasks, Agents, Collaboration"),
    ("Bardeen", "Automation", "Freemium", "https://bardeen.ai", "Automate repetitive tasks with one click.", "Scraping, Shortcuts, Integration"),
    ("Browse AI", "Automation", "Freemium", "https://browse.ai", "Extract and monitor web data easily.", "Scraping, Monitoring, No-Code"),
    ("AgentGPT", "Automation", "Freemium", "https://agentgpt.reworkd.ai", "Assemble, configure, and deploy autonomous AI Agents.", "Browser Agents, Tasks, Goals"),
    ("BabyAGI", "Coding & Development", "Free", "https://github.com/yoheinakajima/babyagi", "An AI-powered task management system.", "Open Source, Autonomous, Scripts"),
    ("AutoGPT", "Coding & Development", "Free", "https://agpt.co", "An experimental open-source attempt to make GPT-4 fully autonomous.", "Agents, Local, Advanced")
]

tools = []
for item in raw_tools:
    name, cat, price, url, desc, tags = item
    
    # Generate a safe slug
    slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    
    domain = url.split("://")[-1].split("/")[0]
    
    # Generate full description
    full_desc = f"{name} is a leading tool in the {cat} space. {desc} Designed to optimize workflows and provide state-of-the-art AI capabilities, it is highly recommended for professionals looking to leverage {tags.split(',')[0]}."
    
    # We use Google's highly reliable favicon service to completely bypass annoying CORS blockers!
    logo_url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
    
    tools.append({
        "Name": name,
        "Slug": slug,
        "Short Description": desc,
        "Category": cat,
        "Pricing": price,
        "URL": url,
        "Logo URL": logo_url,
        "Date Added": today,
        "Full Details": full_desc,
        "Tags": tags,
        "Features": "AI Integration, Cloud Sync, Analytics"
    })

fieldnames = [
    "Name", "Slug", "Short Description", "Category", 
    "Pricing", "URL", "Logo URL", "Date Added", 
    "Full Details", "Tags", "Features"
]

output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "new_tools_to_upload.csv")

with open(output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in tools:
        writer.writerow(row)

print("✅ Generated 80+ top AI tools perfectly formatted in CSV!")
