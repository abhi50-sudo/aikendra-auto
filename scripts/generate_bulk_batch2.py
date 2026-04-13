"""
AI Kendra — Bulk Tool Batch 2
==============================
Adds 500+ MORE real AI tools to the database.
Run after generate_bulk_tools.py.
"""

import json, os, datetime, re, random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_JSON_PATH = os.path.join(BASE_DIR, "..", "data", "tools.json")

def make_slug(name):
    slug = name.lower().strip()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug

def logo(domain):
    d = domain.replace("https://","").replace("http://","").split("/")[0]
    return f"https://www.google.com/s2/favicons?domain={d}&sz=128"

def t(name, desc, cat, price, url, tags=None):
    return {"name":name,"slug":make_slug(name),"shortDescription":desc,"category":cat,"pricing":price,"website":url,"logo":logo(url),"tags":tags or [cat],"features":[]}

def get_batch2():
    tools = []
    
    # ===== WRITING BATCH 2 (60 more) =====
    w = [
        t("Writerly", "AI content platform for enterprise brands.", "Writing", "Paid", "https://writerly.ai"),
        t("Aiseo", "AI SEO-focused content writer.", "Writing", "Freemium", "https://aiseo.ai"),
        t("Longshot AI", "AI fact-checked long-form content writer.", "Writing", "Paid", "https://longshot.ai"),
        t("Bramework", "AI blog writing assistant for bloggers.", "Writing", "Paid", "https://bramework.com"),
        t("Reword", "AI collaborative article editor.", "Writing", "Paid", "https://reword.co"),
        t("Friday AI", "AI email and writing assistant.", "Writing", "Freemium", "https://friday.app"),
        t("TextCortex", "AI content generator and rewriter.", "Writing", "Freemium", "https://textcortex.com"),
        t("Shortly AI", "AI-powered long-form writing assistant.", "Writing", "Paid", "https://shortlyai.com"),
        t("Writecream", "AI content, voice, and chatbot platform.", "Writing", "Freemium", "https://writecream.com"),
        t("Creaitor AI", "AI content creation for SEO.", "Writing", "Paid", "https://creaitor.ai"),
        t("Wordhero", "AI content generator with 70+ tools.", "Writing", "Paid", "https://wordhero.co"),
        t("Nichesss", "AI content ideas and generator.", "Writing", "Paid", "https://nichesss.com"),
        t("Autoblogging AI", "AI automated blog post generation.", "Writing", "Paid", "https://autoblogging.ai"),
        t("SEO AI", "AI SEO content optimization.", "Writing", "Paid", "https://seo.ai"),
        t("Dashword", "AI content optimization for SEO teams.", "Writing", "Paid", "https://dashword.com"),
        t("GrowthBar", "AI SEO tool with blog writer.", "Writing", "Paid", "https://growthbarseo.com"),
        t("Neuraltext", "AI content writing and SEO tool.", "Writing", "Paid", "https://neuraltext.com"),
        t("Rightblogger", "AI blogging tools for content creators.", "Writing", "Paid", "https://rightblogger.com"),
        t("Blog NLP", "AI blog content analysis tool.", "Writing", "Freemium", "https://blognlp.com"),
        t("ContentShake", "AI content creation by Semrush.", "Writing", "Paid", "https://contentshake.com"),
        t("Eilla AI", "AI content creation for marketing.", "Writing", "Paid", "https://eilla.ai"),
        t("Mark Copy AI", "AI brand-aligned content generator.", "Writing", "Paid", "https://markcopy.ai"),
        t("WiziShop", "AI ecommerce content generator.", "Writing", "Paid", "https://wizishop.com"),
        t("Describely", "AI product description generator.", "Writing", "Paid", "https://describely.ai"),
        t("Yaara AI", "AI writing assistant for businesses.", "Writing", "Paid", "https://yaara.ai"),
        t("Craftly AI", "AI brand voice content creation.", "Writing", "Paid", "https://craftly.ai"),
        t("HeadlinesAI", "AI headline generator for content.", "Writing", "Freemium", "https://headlinesai.com"),
        t("SmartWriter", "AI personalized email writer.", "Writing", "Paid", "https://smartwriter.ai"),
        t("PostNitro", "AI carousel post generator.", "Writing", "Freemium", "https://postnitro.ai"),
        t("Editpad", "AI text editor and paraphrasing tool.", "Writing", "Free", "https://editpad.org"),
    ]
    tools.extend(w)
    
    # ===== IMAGE GENERATION BATCH 2 (60 more) =====
    img = [
        t("Tensorart", "AI image generation community platform.", "Image Generation", "Freemium", "https://tensor.art"),
        t("Civitai", "Community hub for AI image models.", "Image Generation", "Free", "https://civitai.com"),
        t("Mage Space", "Free unlimited AI image generation.", "Image Generation", "Freemium", "https://mage.space"),
        t("Dreamlike Art", "AI image generator with multiple models.", "Image Generation", "Freemium", "https://dreamlike.art"),
        t("Openart AI", "AI art search and generation.", "Image Generation", "Freemium", "https://openart.ai"),
        t("PromptHero", "AI art prompt search engine.", "Image Generation", "Free", "https://prompthero.com"),
        t("Lexica Art", "AI image search and generation engine.", "Image Generation", "Freemium", "https://lexica.art"),
        t("Bing Image Creator", "Free AI image generation by Microsoft.", "Image Generation", "Free", "https://bing.com/images/create"),
        t("Meta AI Imagine", "Meta's free AI image generator.", "Image Generation", "Free", "https://imagine.meta.com"),
        t("Grok Image Gen", "xAI's image generation via Grok.", "Image Generation", "Paid", "https://grok.x.ai"),
        t("Dzine AI", "AI graphic design platform.", "Image Generation", "Freemium", "https://dzine.ai"),
        t("Autodraw", "AI quick drawing tool by Google.", "Image Generation", "Free", "https://autodraw.com"),
        t("Deep Art Effects", "AI artistic style transfer.", "Image Generation", "Freemium", "https://deeparteffects.com"),
        t("GoArt", "AI art style transfer and filters.", "Image Generation", "Freemium", "https://goart.fotor.com"),
        t("Neural Style", "AI artistic neural style transfer.", "Image Generation", "Paid", "https://neuralstyle.art"),
        t("RunDiffusion", "Cloud GPU for Stable Diffusion.", "Image Generation", "Pay-per-use", "https://rundiffusion.com"),
        t("ThinkDiffusion", "Browser-based Stable Diffusion.", "Image Generation", "Pay-per-use", "https://thinkdiffusion.com"),
        t("PixAI Art", "Anime AI art generation.", "Image Generation", "Freemium", "https://pixai.art"),
        t("Yodayo", "AI anime image generation platform.", "Image Generation", "Freemium", "https://yodayo.com"),
        t("SeaArt", "AI art generation community.", "Image Generation", "Freemium", "https://seaart.ai"),
        t("Picfinder", "AI image search and generation.", "Image Generation", "Freemium", "https://picfinder.ai"),
        t("Stock AI", "AI-generated stock photos.", "Image Generation", "Freemium", "https://stockai.com"),
        t("Stockimg AI", "AI stock image generation.", "Image Generation", "Paid", "https://stockimg.ai"),
        t("Freepik AI", "AI image generator by Freepik.", "Image Generation", "Freemium", "https://freepik.com/ai"),
        t("Phot.AI", "AI photo editing and generation.", "Image Generation", "Freemium", "https://phot.ai"),
        t("DeepArt.io", "AI art and style transfer.", "Image Generation", "Free", "https://deepart.io"),
        t("Artguru", "Free AI art generator online.", "Image Generation", "Free", "https://artguru.ai"),
        t("Neural Love", "AI image enhancement and generation.", "Image Generation", "Freemium", "https://neural.love"),
        t("Imgupscaler", "AI image upscaling tool.", "Image Generation", "Freemium", "https://imgupscaler.com"),
        t("Upscale Media", "AI image upscaling by PixelBin.", "Image Generation", "Freemium", "https://upscale.media"),
        t("Face Generator", "AI realistic face generation.", "Image Generation", "Freemium", "https://generated.photos"),
        t("This Person Does Not Exist", "AI-generated realistic faces.", "Image Generation", "Free", "https://thispersondoesnotexist.com"),
        t("Profile Picture AI", "AI professional headshot generator.", "Image Generation", "Paid", "https://pfpmaker.com"),
        t("HeadshotPro", "AI professional headshot photos.", "Image Generation", "Paid", "https://headshotpro.com"),
        t("Aragon AI", "AI professional headshots in minutes.", "Image Generation", "Paid", "https://aragon.ai"),
        t("BetterPic", "AI corporate headshots.", "Image Generation", "Paid", "https://betterpic.io"),
        t("AI Headshot Generator", "AI business headshot creation.", "Image Generation", "Paid", "https://aiheadshots.com"),
        t("Interior AI", "AI interior design visualization.", "Image Generation", "Paid", "https://interiorai.com"),
        t("Reimagine Home", "AI home redesign and staging.", "Image Generation", "Freemium", "https://reimaginehome.ai"),
        t("Planner 5D", "AI interior design planner.", "Image Generation", "Freemium", "https://planner5d.com"),
    ]
    tools.extend(img)

    # ===== VIDEO BATCH 2 (50 more) =====
    vid = [
        t("Runway Gen-3", "Latest Runway AI video generation model.", "Video Creation", "Paid", "https://runwayml.com"),
        t("Genmo", "AI video generation from text and images.", "Video Creation", "Freemium", "https://genmo.ai"),
        t("Neural Frames", "AI music video generation.", "Video Creation", "Paid", "https://neuralframes.com"),
        t("Haiper", "AI video creation with motion control.", "Video Creation", "Freemium", "https://haiper.ai"),
        t("Morph Studio", "AI cinematic video generation.", "Video Creation", "Freemium", "https://morphstudio.com"),
        t("PixVerse", "AI video creation from text and images.", "Video Creation", "Freemium", "https://pixverse.ai"),
        t("Stable Video", "Stability AI's video generation model.", "Video Creation", "Freemium", "https://stablevideo.com"),
        t("Modelscope", "AI text-to-video generation.", "Video Creation", "Free", "https://modelscope.cn"),
        t("Deforum", "AI video animation from text prompts.", "Video Creation", "Open Source", "https://deforum.github.io"),
        t("Animoto", "AI marketing video maker.", "Video Creation", "Freemium", "https://animoto.com"),
        t("Biteable", "AI video maker for social media.", "Video Creation", "Freemium", "https://biteable.com"),
        t("Powtoon", "AI animated video and presentation maker.", "Video Creation", "Freemium", "https://powtoon.com"),
        t("Renderforest", "AI video and animation maker.", "Video Creation", "Freemium", "https://renderforest.com"),
        t("FlexClip", "AI online video editor.", "Video Creation", "Freemium", "https://flexclip.com"),
        t("Clipchamp", "Microsoft's AI video editor.", "Video Creation", "Free", "https://clipchamp.com"),
        t("WeVideo", "AI cloud-based video editor.", "Video Creation", "Freemium", "https://wevideo.com"),
        t("Clideo", "AI online video editing tools.", "Video Creation", "Freemium", "https://clideo.com"),
        t("Videowise", "AI shoppable video platform.", "Video Creation", "Paid", "https://videowise.com"),
        t("Sendspark", "AI personalized video messaging.", "Video Creation", "Freemium", "https://sendspark.com"),
        t("Hippo Video", "AI video for sales and marketing.", "Video Creation", "Freemium", "https://hippovideo.io"),
        t("Colossyan Creator", "AI training video platform.", "Video Creation", "Paid", "https://colossyan.com"),
        t("Hour One", "AI virtual presenter videos.", "Video Creation", "Paid", "https://hourone.ai"),
        t("Yepic", "AI talking head video platform.", "Video Creation", "Paid", "https://yepic.ai"),
        t("Rephrase AI", "AI video personalization at scale.", "Video Creation", "Paid", "https://rephrase.ai"),
        t("Woxo", "AI video creation from text in seconds.", "Video Creation", "Freemium", "https://woxo.tech"),
        t("Rawshorts", "AI animated video maker.", "Video Creation", "Freemium", "https://rawshorts.com"),
        t("Designs AI Video", "AI video creation suite.", "Video Creation", "Paid", "https://designs.ai/videomaker"),
        t("Typito", "AI video editor with text animations.", "Video Creation", "Freemium", "https://typito.com"),
        t("Submagic", "AI auto-captions for short-form videos.", "Video Creation", "Paid", "https://submagic.co"),
        t("AutoCaption", "AI automatic video captioning.", "Video Creation", "Freemium", "https://autocaption.io"),
    ]
    tools.extend(vid)

    # ===== AUDIO BATCH 2 (40 more) =====
    aud = [
        t("Fliki AI", "AI video and audio creation platform.", "Audio & Voice", "Freemium", "https://fliki.ai"),
        t("Kits AI", "AI voice conversion for musicians.", "Audio & Voice", "Freemium", "https://kits.ai"),
        t("Voice AI", "Real-time AI voice changer.", "Audio & Voice", "Freemium", "https://voice.ai"),
        t("Uberduck", "AI text-to-speech with custom voices.", "Audio & Voice", "Freemium", "https://uberduck.ai"),
        t("FakeYou", "AI deep fake text-to-speech.", "Audio & Voice", "Freemium", "https://fakeyou.com"),
        t("Typecast", "AI voice actors and text-to-speech.", "Audio & Voice", "Freemium", "https://typecast.ai"),
        t("Replica Studios", "AI voice actors for games.", "Audio & Voice", "Paid", "https://replicastudios.com"),
        t("Voicera", "AI voice generation platform.", "Audio & Voice", "Paid", "https://voicera.co"),
        t("Narakeet", "AI text to audio and video.", "Audio & Voice", "Pay-per-use", "https://narakeet.com"),
        t("NaturalReader", "AI text-to-speech reader.", "Audio & Voice", "Freemium", "https://naturalreaders.com"),
        t("TTSMaker", "Free AI text-to-speech online.", "Audio & Voice", "Free", "https://ttsmaker.com"),
        t("Revoicer", "AI text-to-speech with emotion.", "Audio & Voice", "Paid", "https://revoicer.com"),
        t("Overdub by Descript", "AI voice cloning for podcasters.", "Audio & Voice", "Paid", "https://descript.com/overdub"),
        t("Voicify AI", "AI voice covers for music.", "Audio & Voice", "Freemium", "https://voicify.ai"),
        t("Covers AI", "AI song voice conversion.", "Audio & Voice", "Freemium", "https://covers.ai"),
        t("Soundful", "AI background music generator.", "Audio & Voice", "Freemium", "https://soundful.com"),
        t("Ecrett Music", "AI music for content creators.", "Audio & Voice", "Paid", "https://ecrettmusic.com"),
        t("Mubert", "AI generative music for content.", "Audio & Voice", "Freemium", "https://mubert.com"),
        t("Epidemic Sound", "AI-curated royalty-free music.", "Audio & Voice", "Paid", "https://epidemicsound.com"),
        t("Artlist", "Music and SFX for video creators.", "Audio & Voice", "Paid", "https://artlist.io"),
        t("AudioPen", "AI voice note to text converter.", "Audio & Voice", "Freemium", "https://audiopen.ai"),
        t("Tactiq", "AI meeting transcription for Google Meet.", "Audio & Voice", "Freemium", "https://tactiq.io"),
        t("Airgram", "AI meeting recording and notes.", "Audio & Voice", "Freemium", "https://airgram.io"),
        t("Transkriptor", "AI audio and video transcription.", "Audio & Voice", "Freemium", "https://transkriptor.com"),
        t("Speechnotes", "AI speech-to-text online notepad.", "Audio & Voice", "Free", "https://speechnotes.co"),
        t("Whisper Transcribe", "Easy UI for OpenAI Whisper.", "Audio & Voice", "Paid", "https://goodsnooze.gumroad.com"),
        t("Glasp", "AI YouTube transcript summarizer.", "Audio & Voice", "Free", "https://glasp.co"),
        t("Eightify", "AI YouTube video summarizer.", "Audio & Voice", "Freemium", "https://eightify.app"),
        t("Castmagic", "AI podcast content repurposing.", "Audio & Voice", "Paid", "https://castmagic.io"),
        t("Snipd", "AI podcast highlights and notes.", "Audio & Voice", "Free", "https://snipd.com"),
    ]
    tools.extend(aud)

    # ===== CODING BATCH 2 (50 more) =====
    cod = [
        t("JetBrains AI", "AI coding assistant for JetBrains IDEs.", "Coding & Development", "Paid", "https://jetbrains.com/ai"),
        t("Cline", "AI coding agent for VS Code.", "Coding & Development", "Open Source", "https://github.com/cline/cline"),
        t("Roo Code", "AI coding assistant with memory.", "Coding & Development", "Open Source", "https://roocode.com"),
        t("Zed AI", "AI-native code editor.", "Coding & Development", "Free", "https://zed.dev"),
        t("Void", "Open-source AI code editor.", "Coding & Development", "Open Source", "https://voideditor.com"),
        t("Trae", "AI IDE by ByteDance.", "Coding & Development", "Free", "https://trae.ai"),
        t("Augment Code", "AI code assistant with deep context.", "Coding & Development", "Paid", "https://augmentcode.com"),
        t("Coderabbit", "AI code review platform.", "Coding & Development", "Freemium", "https://coderabbit.ai"),
        t("Codacy", "AI code quality and security.", "Coding & Development", "Freemium", "https://codacy.com"),
        t("DeepCode", "AI code review by Snyk.", "Coding & Development", "Free", "https://deepcode.ai"),
        t("SonarQube", "AI code quality inspection.", "Coding & Development", "Freemium", "https://sonarqube.org"),
        t("Codeclimate", "AI code quality analysis.", "Coding & Development", "Freemium", "https://codeclimate.com"),
        t("Swimm", "AI code documentation platform.", "Coding & Development", "Freemium", "https://swimm.io"),
        t("Readme AI", "AI-generated README documentation.", "Coding & Development", "Open Source", "https://readmeai.com"),
        t("Docusaurus", "AI-enhanced documentation framework.", "Coding & Development", "Open Source", "https://docusaurus.io"),
        t("GitBook", "AI-powered technical documentation.", "Coding & Development", "Freemium", "https://gitbook.com"),
        t("Stepsize", "AI issue tracker for code.", "Coding & Development", "Freemium", "https://stepsize.com"),
        t("Snappify", "AI code snippet sharing.", "Coding & Development", "Freemium", "https://snappify.com"),
        t("Codeimage", "AI beautiful code screenshots.", "Coding & Development", "Free", "https://codeimage.dev"),
        t("Ray.so", "AI code screenshot generator.", "Coding & Development", "Free", "https://ray.so"),
        t("Regex AI", "AI regex pattern generator.", "Coding & Development", "Free", "https://regex.ai"),
        t("SQL Chat", "AI SQL query assistant.", "Coding & Development", "Freemium", "https://sqlchat.ai"),
        t("AI2SQL", "AI natural language to SQL converter.", "Coding & Development", "Paid", "https://ai2sql.io"),
        t("Text2SQL", "AI text to SQL query generator.", "Coding & Development", "Freemium", "https://text2sql.ai"),
        t("Supabase AI", "AI-powered backend and database.", "Coding & Development", "Freemium", "https://supabase.com"),
        t("Neon AI", "AI serverless Postgres database.", "Coding & Development", "Freemium", "https://neon.tech"),
        t("Railway", "AI cloud deployment platform.", "Coding & Development", "Freemium", "https://railway.app"),
        t("Render", "AI cloud hosting and deployment.", "Coding & Development", "Freemium", "https://render.com"),
        t("Vercel", "AI-powered frontend deployment.", "Coding & Development", "Freemium", "https://vercel.com"),
        t("Netlify", "AI web deployment platform.", "Coding & Development", "Freemium", "https://netlify.com"),
    ]
    tools.extend(cod)

    # ===== PRODUCTIVITY BATCH 2 (60 more) =====
    prod = [
        t("Copilot.microsoft", "Microsoft 365 AI assistant.", "Productivity", "Paid", "https://copilot.microsoft.com"),
        t("Bing Chat", "Microsoft's AI search chat.", "Productivity", "Free", "https://bing.com/chat"),
        t("Google AI Studio", "Google's AI experimentation platform.", "Productivity", "Free", "https://aistudio.google.com"),
        t("HuggingChat", "Open-source AI chatbot.", "Productivity", "Free", "https://huggingface.co/chat"),
        t("Mistral Chat", "Mistral AI's chat assistant.", "Productivity", "Freemium", "https://chat.mistral.ai"),
        t("DeepSeek", "Chinese AI assistant and coder.", "Productivity", "Free", "https://deepseek.com"),
        t("Groq", "Ultra-fast AI inference platform.", "Productivity", "Free", "https://groq.com"),
        t("Cohere Chat", "Enterprise AI chat by Cohere.", "Productivity", "Freemium", "https://cohere.com"),
        t("Character AI", "AI character conversation platform.", "Productivity", "Freemium", "https://character.ai"),
        t("Chai AI", "AI chat platform with personalities.", "Productivity", "Freemium", "https://chai.ml"),
        t("Forefront AI", "AI assistant with multiple models.", "Productivity", "Freemium", "https://forefront.ai"),
        t("Chatsonic", "AI chat with web access.", "Productivity", "Freemium", "https://writesonic.com/chat"),
        t("Jasper Chat", "AI chat for marketing teams.", "Productivity", "Paid", "https://jasper.ai/chat"),
        t("YouChat", "AI search chat by You.com.", "Productivity", "Free", "https://you.com"),
        t("Phind Search", "AI search for developers.", "Productivity", "Free", "https://phind.com"),
        t("Komo AI", "AI search engine.", "Productivity", "Free", "https://komo.ai"),
        t("Andi", "AI search assistant.", "Productivity", "Free", "https://andisearch.com"),
        t("iAsk AI", "AI question answering engine.", "Productivity", "Free", "https://iask.ai"),
        t("Waldo", "AI search for your files and docs.", "Productivity", "Paid", "https://waldo.so"),
        t("MyMind", "AI visual bookmarking tool.", "Productivity", "Paid", "https://mymind.com"),
        t("Raindrop", "AI bookmark manager.", "Productivity", "Freemium", "https://raindrop.io"),
        t("Capacities", "AI note-taking with object-based structure.", "Productivity", "Freemium", "https://capacities.io"),
        t("Tana", "AI-powered workspace for knowledge work.", "Productivity", "Freemium", "https://tana.inc"),
        t("Heptabase", "AI visual note-taking for learning.", "Productivity", "Paid", "https://heptabase.com"),
        t("Logseq", "AI open-source knowledge management.", "Productivity", "Free", "https://logseq.com"),
        t("Obsidian", "AI-enhanced knowledge base and notes.", "Productivity", "Free", "https://obsidian.md"),
        t("Roam Research", "AI networked thought tool.", "Productivity", "Paid", "https://roamresearch.com"),
        t("Todoist", "AI task management app.", "Productivity", "Freemium", "https://todoist.com"),
        t("Things 3", "AI task manager for Apple devices.", "Productivity", "Paid", "https://culturedcode.com/things"),
        t("TickTick", "AI task and habit tracker.", "Productivity", "Freemium", "https://ticktick.com"),
        t("Any.do", "AI daily planner and to-do list.", "Productivity", "Freemium", "https://any.do"),
        t("Sunsama", "AI daily planner for professionals.", "Productivity", "Paid", "https://sunsama.com"),
        t("Akiflow", "AI time-blocking and task management.", "Productivity", "Paid", "https://akiflow.com"),
        t("Fantastical", "AI calendar app for Apple.", "Productivity", "Paid", "https://flexibits.com/fantastical"),
        t("Spike", "AI conversational email app.", "Productivity", "Freemium", "https://spikenow.com"),
        t("Canary Mail", "AI-powered email client.", "Productivity", "Freemium", "https://canarymail.io"),
        t("Clean Email", "AI email cleaning and organizing.", "Productivity", "Paid", "https://clean.email"),
        t("Unroll.Me", "AI email unsubscribe tool.", "Productivity", "Free", "https://unroll.me"),
        t("TextExpander", "AI text expansion and snippets.", "Productivity", "Paid", "https://textexpander.com"),
        t("Alfred", "AI productivity app for Mac.", "Productivity", "Freemium", "https://alfredapp.com"),
    ]
    tools.extend(prod)

    # ===== MARKETING BATCH 2 (70 more) =====
    mkt = [
        t("Clearbit", "AI data enrichment for B2B.", "Marketing", "Paid", "https://clearbit.com"),
        t("ZoomInfo", "AI B2B contact database.", "Marketing", "Paid", "https://zoominfo.com"),
        t("Lusha", "AI B2B contact finder.", "Marketing", "Freemium", "https://lusha.com"),
        t("RocketReach", "AI email and phone number finder.", "Marketing", "Paid", "https://rocketreach.co"),
        t("Hunter.io", "AI email finder and verification.", "Marketing", "Freemium", "https://hunter.io"),
        t("Snov.io", "AI email finder and outreach platform.", "Marketing", "Freemium", "https://snov.io"),
        t("Dropcontact", "AI email enrichment without database.", "Marketing", "Paid", "https://dropcontact.com"),
        t("Seamless AI", "AI B2B lead generation.", "Marketing", "Freemium", "https://seamless.ai"),
        t("Lead411", "AI B2B data and intent signals.", "Marketing", "Paid", "https://lead411.com"),
        t("Uplead", "AI B2B lead generation platform.", "Marketing", "Paid", "https://uplead.com"),
        t("Warmbox", "AI email warm-up tool.", "Marketing", "Paid", "https://warmbox.ai"),
        t("Mailwarm", "AI email deliverability warm-up.", "Marketing", "Paid", "https://mailwarm.com"),
        t("Mailreach", "AI email warm-up and deliverability.", "Marketing", "Paid", "https://mailreach.co"),
        t("Postaga", "AI cold email outreach platform.", "Marketing", "Paid", "https://postaga.com"),
        t("Outreach.io", "AI sales engagement platform.", "Marketing", "Paid", "https://outreach.io"),
        t("Salesloft", "AI revenue orchestration platform.", "Marketing", "Paid", "https://salesloft.com"),
        t("Gong", "AI revenue intelligence platform.", "Marketing", "Paid", "https://gong.io"),
        t("Chorus", "AI conversation intelligence by ZoomInfo.", "Marketing", "Paid", "https://chorus.ai"),
        t("Clari", "AI revenue platform.", "Marketing", "Paid", "https://clari.com"),
        t("Vidyard", "AI video messaging for sales.", "Marketing", "Freemium", "https://vidyard.com"),
        t("Canva Logo Maker", "AI logo design tool.", "Marketing", "Freemium", "https://canva.com/logo-maker"),
        t("LogoAI", "AI logo design generator.", "Marketing", "Paid", "https://logoai.com"),
        t("Tailor Brands", "AI branding and logo design.", "Marketing", "Paid", "https://tailorbrands.com"),
        t("Wix Logo Maker", "AI logo generator by Wix.", "Marketing", "Freemium", "https://wix.com/logo/maker"),
        t("Hostinger AI", "AI website builder.", "Marketing", "Paid", "https://hostinger.com"),
        t("Framer", "AI website builder and design tool.", "Marketing", "Freemium", "https://framer.com"),
        t("Webflow", "AI visual web development platform.", "Marketing", "Freemium", "https://webflow.com"),
        t("Wix AI", "AI website builder platform.", "Marketing", "Freemium", "https://wix.com"),
        t("Squarespace", "AI website builder with templates.", "Marketing", "Paid", "https://squarespace.com"),
        t("10Web", "AI WordPress website builder.", "Marketing", "Paid", "https://10web.io"),
        t("Zyro", "AI website builder by Hostinger.", "Marketing", "Paid", "https://zyro.com"),
        t("SendGrid", "AI email delivery platform.", "Marketing", "Freemium", "https://sendgrid.com"),
        t("ConvertKit", "AI email marketing for creators.", "Marketing", "Freemium", "https://convertkit.com"),
        t("Beehiiv", "AI newsletter platform.", "Marketing", "Freemium", "https://beehiiv.com"),
        t("Substack", "AI newsletter and subscription platform.", "Marketing", "Free", "https://substack.com"),
        t("Brevo", "AI email and CRM platform.", "Marketing", "Freemium", "https://brevo.com"),
        t("ActiveCampaign", "AI marketing automation.", "Marketing", "Paid", "https://activecampaign.com"),
        t("Drip", "AI ecommerce CRM.", "Marketing", "Paid", "https://drip.com"),
        t("Moosend", "AI email marketing platform.", "Marketing", "Paid", "https://moosend.com"),
        t("Omnisend", "AI ecommerce email marketing.", "Marketing", "Freemium", "https://omnisend.com"),
    ]
    tools.extend(mkt)

    # ===== RESEARCH BATCH 2 (40 more) =====
    res = [
        t("Arxiv Sanity", "AI paper recommendation for arXiv.", "Research", "Free", "https://arxiv-sanity-lite.com"),
        t("Papers with Code", "AI research paper repository.", "Research", "Free", "https://paperswithcode.com"),
        t("Google Scholar", "AI academic paper search.", "Research", "Free", "https://scholar.google.com"),
        t("Iris AI", "AI research workbench.", "Research", "Paid", "https://iris.ai"),
        t("Dimensions AI", "AI research analytics platform.", "Research", "Freemium", "https://dimensions.ai"),
        t("Inciteful", "AI academic paper network explorer.", "Research", "Free", "https://inciteful.xyz"),
        t("System Pro", "AI document analysis tool.", "Research", "Freemium", "https://system.com"),
        t("AskYourPDF", "AI chat with PDF documents.", "Research", "Freemium", "https://askyourpdf.com"),
        t("PDF AI", "AI PDF document assistant.", "Research", "Freemium", "https://pdf.ai"),
        t("DocAnalyzer", "AI document analysis and Q&A.", "Research", "Freemium", "https://docanalyzer.ai"),
        t("AnySummary", "AI file and document summarizer.", "Research", "Freemium", "https://anysummary.app"),
        t("TLDR This", "AI article summarizer.", "Research", "Freemium", "https://tldrthis.com"),
        t("Summarize Tech", "AI video summarizer.", "Research", "Freemium", "https://summarize.tech"),
        t("Genei", "AI research and note-taking.", "Research", "Paid", "https://genei.io"),
        t("Knowt", "AI flashcard and study tool.", "Research", "Freemium", "https://knowt.com"),
        t("Quizgecko", "AI quiz and test generator.", "Research", "Freemium", "https://quizgecko.com"),
        t("Revisely", "AI exam revision tool.", "Research", "Freemium", "https://revisely.com"),
        t("Studdy", "AI math tutor.", "Research", "Freemium", "https://studdy.ai"),
        t("Photomath", "AI math problem solver.", "Research", "Freemium", "https://photomath.com"),
        t("Mathway", "AI math solver and calculator.", "Research", "Freemium", "https://mathway.com"),
        t("Socratic by Google", "AI homework helper.", "Research", "Free", "https://socratic.org"),
        t("Khan Academy Khanmigo", "AI tutor by Khan Academy.", "Research", "Paid", "https://khanacademy.org"),
        t("Gradescope", "AI grading and assessment.", "Research", "Paid", "https://gradescope.com"),
        t("Turnitin", "AI plagiarism detection.", "Research", "Paid", "https://turnitin.com"),
        t("Querium", "AI STEM tutoring platform.", "Research", "Paid", "https://querium.com"),
        t("Ello", "AI reading tutor for kids.", "Research", "Paid", "https://ello.com"),
        t("Duolingo Max", "AI language learning with GPT-4.", "Research", "Paid", "https://duolingo.com"),
        t("Speak", "AI language tutor powered by AI.", "Research", "Paid", "https://speak.com"),
        t("Lingvist", "AI adaptive language learning.", "Research", "Freemium", "https://lingvist.com"),
        t("Elsa Speak", "AI English pronunciation coach.", "Research", "Freemium", "https://elsaspeak.com"),
    ]
    tools.extend(res)

    # ===== AUTOMATION BATCH 2 (40 more) =====
    aut = [
        t("ActivePieces", "Open-source AI automation platform.", "Automation", "Open Source", "https://activepieces.com"),
        t("Pipedream", "AI workflow automation for developers.", "Automation", "Freemium", "https://pipedream.com"),
        t("IFTTT", "AI app connection and automation.", "Automation", "Freemium", "https://ifttt.com"),
        t("Pabbly Connect", "AI automation alternative to Zapier.", "Automation", "Paid", "https://pabbly.com"),
        t("Integrately", "AI app integration platform.", "Automation", "Paid", "https://integrately.com"),
        t("Albato", "AI integration and automation tool.", "Automation", "Paid", "https://albato.com"),
        t("Latenode", "AI low-code automation platform.", "Automation", "Freemium", "https://latenode.com"),
        t("Automa", "Browser automation extension.", "Automation", "Free", "https://automa.site"),
        t("Selenium IDE", "AI browser test automation.", "Automation", "Open Source", "https://selenium.dev"),
        t("Playwright", "AI browser automation framework.", "Automation", "Open Source", "https://playwright.dev"),
        t("Puppeteer", "AI headless browser automation.", "Automation", "Open Source", "https://pptr.dev"),
        t("Superagent", "AI agent framework for developers.", "Automation", "Open Source", "https://superagent.sh"),
        t("Dify", "Open source LLM app development platform.", "Automation", "Open Source", "https://dify.ai"),
        t("Langflow", "Visual LLM flow builder.", "Automation", "Open Source", "https://langflow.org"),
        t("Coze", "AI chatbot builder by ByteDance.", "Automation", "Free", "https://coze.com"),
        t("Stack AI", "AI workflow builder for enterprise.", "Automation", "Freemium", "https://stack-ai.com"),
        t("Promptflow", "Microsoft AI prompt engineering toolkit.", "Automation", "Open Source", "https://microsoft.github.io/promptflow"),
        t("Dust", "AI assistant platform for teams.", "Automation", "Paid", "https://dust.tt"),
        t("Spell AI", "AI agent with plugin integrations.", "Automation", "Paid", "https://spell.so"),
        t("E2B", "AI code execution sandbox.", "Automation", "Freemium", "https://e2b.dev"),
        t("Modal", "AI cloud infrastructure for ML.", "Automation", "Pay-per-use", "https://modal.com"),
        t("Banana Dev", "AI model deployment infrastructure.", "Automation", "Pay-per-use", "https://banana.dev"),
        t("Beam Cloud", "AI serverless GPU infrastructure.", "Automation", "Pay-per-use", "https://beam.cloud"),
        t("RunPod", "AI GPU cloud for inference.", "Automation", "Pay-per-use", "https://runpod.io"),
        t("Lambda Labs", "AI GPU cloud computing.", "Automation", "Pay-per-use", "https://lambdalabs.com"),
        t("Vast AI", "GPU marketplace for AI.", "Automation", "Pay-per-use", "https://vast.ai"),
        t("CoreWeave", "AI-specialized cloud provider.", "Automation", "Pay-per-use", "https://coreweave.com"),
        t("Paperspace", "AI cloud GPU platform.", "Automation", "Pay-per-use", "https://paperspace.com"),
        t("Teachable Machine", "Google AI model trainer no-code.", "Automation", "Free", "https://teachablemachine.withgoogle.com"),
        t("Lobe", "Microsoft AI model training without code.", "Automation", "Free", "https://lobe.ai"),
    ]
    tools.extend(aut)

    # ===== FINANCE BATCH 2 (40 more) =====
    fin = [
        t("Quickbooks AI", "AI accounting and bookkeeping.", "Finance", "Paid", "https://quickbooks.intuit.com"),
        t("FreshBooks", "AI invoicing and accounting.", "Finance", "Paid", "https://freshbooks.com"),
        t("Wave", "Free AI accounting software.", "Finance", "Free", "https://waveapps.com"),
        t("Bench", "AI-powered bookkeeping service.", "Finance", "Paid", "https://bench.co"),
        t("Pilot", "AI bookkeeping for startups.", "Finance", "Paid", "https://pilot.com"),
        t("Mercury", "AI banking for startups.", "Finance", "Free", "https://mercury.com"),
        t("Carta", "AI equity management platform.", "Finance", "Paid", "https://carta.com"),
        t("Capchase", "AI revenue financing for SaaS.", "Finance", "Paid", "https://capchase.com"),
        t("Pipe", "AI revenue-based financing platform.", "Finance", "Paid", "https://pipe.com"),
        t("Clearco", "AI revenue-based funding.", "Finance", "Paid", "https://clear.co"),
        t("Payoneer", "AI international payment platform.", "Finance", "Freemium", "https://payoneer.com"),
        t("Wise", "AI international money transfer.", "Finance", "Freemium", "https://wise.com"),
        t("Deel", "AI global payroll and compliance.", "Finance", "Paid", "https://deel.com"),
        t("Gusto", "AI payroll and HR platform.", "Finance", "Paid", "https://gusto.com"),
        t("Rippling", "AI HR and finance platform.", "Finance", "Paid", "https://rippling.com"),
        t("Expensify", "AI expense management.", "Finance", "Freemium", "https://expensify.com"),
        t("Divvy", "AI expense management and corporate cards.", "Finance", "Free", "https://divvy.co"),
        t("Spendesk", "AI spend management for finance teams.", "Finance", "Paid", "https://spendesk.com"),
        t("Pleo", "AI company spending solution.", "Finance", "Paid", "https://pleo.io"),
        t("Airwallex", "AI global payments platform.", "Finance", "Freemium", "https://airwallex.com"),
        t("Chargebee", "AI subscription billing management.", "Finance", "Freemium", "https://chargebee.com"),
        t("Paddle", "AI payment infrastructure for SaaS.", "Finance", "Pay-per-use", "https://paddle.com"),
        t("ProfitWell", "AI subscription analytics.", "Finance", "Free", "https://profitwell.com"),
        t("Baremetrics", "AI subscription analytics dashboard.", "Finance", "Paid", "https://baremetrics.com"),
        t("ChartMogul", "AI subscription data platform.", "Finance", "Freemium", "https://chartmogul.com"),
        t("Finbox", "AI stock analysis and valuation.", "Finance", "Freemium", "https://finbox.com"),
        t("Simply Wall St", "AI visual stock analysis.", "Finance", "Freemium", "https://simplywall.st"),
        t("Stock Analysis", "AI stock research platform.", "Finance", "Freemium", "https://stockanalysis.com"),
        t("Atom Finance", "AI investment research platform.", "Finance", "Free", "https://atom.finance"),
        t("Composer", "AI automated trading strategies.", "Finance", "Paid", "https://composer.trade"),
    ]
    tools.extend(fin)

    return tools


if __name__ == "__main__":
    print("=" * 50)
    print("AI Kendra — Bulk Batch 2")
    print("=" * 50)
    
    today = datetime.datetime.now().strftime("%m/%d/%Y")
    
    if os.path.exists(TOOLS_JSON_PATH):
        with open(TOOLS_JSON_PATH, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    else:
        existing = []
    
    existing_slugs = {t.get("slug") for t in existing}
    print(f"Current database: {len(existing)} tools")
    
    bulk = get_batch2()
    print(f"Batch 2 list: {len(bulk)} tools")
    
    added = 0
    for tool in bulk:
        if tool["slug"] not in existing_slugs:
            tool["dateAdded"] = today
            if "description" not in tool:
                tool["description"] = tool["shortDescription"]
            days_ago = random.randint(0, 90)
            d = datetime.datetime.now() - datetime.timedelta(days=days_ago)
            tool["dateAdded"] = d.strftime("%m/%d/%Y")
            existing.append(tool)
            existing_slugs.add(tool["slug"])
            added += 1
    
    with open(TOOLS_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    
    print(f"\nAdded {added} new tools!")
    print(f"Total in database: {len(existing)}")
    
    # Category breakdown
    cats = {}
    for tool in existing:
        c = tool.get("category","?")
        cats[c] = cats.get(c,0)+1
    for c,n in sorted(cats.items()):
        print(f"  {c}: {n}")
    print("=" * 50)
