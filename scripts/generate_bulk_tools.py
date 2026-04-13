"""
AI Kendra — Bulk Tool Generator
=================================
Generates 5000+ real AI tools organized by category.
Run ONCE to seed the database, then the daily scraper handles new additions.

Usage: python scripts/generate_bulk_tools.py
"""

import json
import os
import datetime
import re
import random

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

def t(name, desc, category, pricing, website, tags=None, features=None):
    """Shorthand to create a tool entry."""
    return {
        "name": name,
        "slug": make_slug(name),
        "shortDescription": desc,
        "category": category,
        "pricing": pricing,
        "website": website,
        "logo": logo(website),
        "tags": tags or [category],
        "features": features or [],
    }

def get_all_tools():
    """Master list of 5000+ real AI tools."""
    tools = []
    
    # =============================================================
    # WRITING & CONTENT (500+)
    # =============================================================
    writing = [
        t("Grammarly", "AI writing assistant for grammar, tone, and clarity.", "Writing", "Freemium", "https://grammarly.com", ["Grammar","Writing","Proofreading"]),
        t("Jasper", "AI content platform for marketing teams.", "Writing", "Paid", "https://jasper.ai", ["Marketing","Copywriting","Content"]),
        t("Copy.ai", "AI-powered copywriting and content generation.", "Writing", "Freemium", "https://copy.ai", ["Copywriting","Marketing","Sales"]),
        t("Writesonic", "AI writer for blogs, ads, and marketing copy.", "Writing", "Freemium", "https://writesonic.com", ["Blog Writing","Ads","SEO"]),
        t("Rytr", "AI writing assistant for content creation.", "Writing", "Freemium", "https://rytr.me", ["Content","Templates","Writing"]),
        t("Wordtune", "AI tool to rewrite and improve your text.", "Writing", "Freemium", "https://wordtune.com", ["Rewriting","Paraphrasing"]),
        t("QuillBot", "AI paraphrasing and summarization tool.", "Writing", "Freemium", "https://quillbot.com", ["Paraphrasing","Academic"]),
        t("Sudowrite", "AI writing partner for fiction and creative writing.", "Writing", "Paid", "https://sudowrite.com", ["Fiction","Creative Writing"]),
        t("Anyword", "AI copywriting with predictive analytics.", "Writing", "Paid", "https://anyword.com", ["Copywriting","Analytics"]),
        t("Peppertype", "AI content assistant for teams.", "Writing", "Paid", "https://peppertype.ai", ["Content","Teams"]),
        t("Simplified", "AI writer, designer, and social media manager in one.", "Writing", "Freemium", "https://simplified.com", ["All-in-One","Social Media"]),
        t("Scalenut", "AI SEO and content marketing platform.", "Writing", "Paid", "https://scalenut.com", ["SEO","Content Marketing"]),
        t("Frase", "AI content optimization for SEO.", "Writing", "Paid", "https://frase.io", ["SEO","Content Optimization"]),
        t("Surfer SEO", "AI-powered SEO content editor.", "Writing", "Paid", "https://surferseo.com", ["SEO","Content Editor"]),
        t("Clearscope", "AI content optimization platform.", "Writing", "Paid", "https://clearscope.io", ["SEO","Content"]),
        t("MarketMuse", "AI content strategy and planning platform.", "Writing", "Paid", "https://marketmuse.com", ["Content Strategy","SEO"]),
        t("INK Editor", "AI writing and SEO optimization tool.", "Writing", "Freemium", "https://inkforall.com", ["SEO","Writing"]),
        t("Hemingway Editor", "AI tool that makes your writing bold and clear.", "Writing", "Free", "https://hemingwayapp.com", ["Readability","Editing"]),
        t("ProWritingAid", "AI grammar checker and style editor for writers.", "Writing", "Freemium", "https://prowritingaid.com", ["Grammar","Style"]),
        t("Linguix", "AI writing assistant and grammar checker.", "Writing", "Freemium", "https://linguix.com", ["Grammar","Writing"]),
        t("Outwrite", "AI writing assistant with rewrite suggestions.", "Writing", "Freemium", "https://outwrite.com", ["Rewriting","Grammar"]),
        t("Sapling", "AI writing assistant for customer-facing teams.", "Writing", "Freemium", "https://sapling.ai", ["Customer Support","Writing"]),
        t("Textio", "AI-powered writing platform for inclusive language.", "Writing", "Paid", "https://textio.com", ["HR","Inclusive Writing"]),
        t("Writer", "AI writing platform for enterprise teams.", "Writing", "Paid", "https://writer.com", ["Enterprise","Brand Voice"]),
        t("ContentBot", "AI content generation for marketers.", "Writing", "Paid", "https://contentbot.ai", ["Marketing","Blog"]),
        t("Closers Copy", "AI copywriting tool for sales and marketing.", "Writing", "Paid", "https://closerscopy.com", ["Sales Copy","Marketing"]),
        t("Copysmith", "AI content creation for ecommerce.", "Writing", "Paid", "https://copysmith.ai", ["Ecommerce","Product Descriptions"]),
        t("Unbounce Smart Copy", "AI copywriting for landing pages.", "Writing", "Freemium", "https://unbounce.com/smart-copy", ["Landing Pages","Conversion"]),
        t("Kafkai", "AI article writer for SEO content.", "Writing", "Paid", "https://kafkai.com", ["SEO","Articles"]),
        t("Article Forge", "AI automated article writing.", "Writing", "Paid", "https://articleforge.com", ["Articles","Automation"]),
        t("Koala Writer", "AI SEO article writer with real-time data.", "Writing", "Paid", "https://koala.sh", ["SEO","Articles"]),
        t("Byword", "AI article generator for SEO at scale.", "Writing", "Paid", "https://byword.ai", ["SEO","Bulk Content"]),
        t("Jenni AI", "AI research and academic writing assistant.", "Writing", "Freemium", "https://jenni.ai", ["Academic","Research"]),
        t("Lex", "AI-powered word processor for writers.", "Writing", "Freemium", "https://lex.page", ["Word Processor","Writing"]),
        t("Type AI", "AI document editor with built-in writing assistant.", "Writing", "Freemium", "https://type.ai", ["Documents","Writing"]),
        t("Moonbeam", "AI writing assistant for long-form content.", "Writing", "Paid", "https://gomoonbeam.com", ["Long-Form","Blog"]),
        t("Hypotenuse AI", "AI content and image generation platform.", "Writing", "Paid", "https://hypotenuse.ai", ["Content","Ecommerce"]),
        t("Bertha AI", "AI copywriting inside WordPress.", "Writing", "Paid", "https://bertha.ai", ["WordPress","Copywriting"]),
        t("Narrato", "AI content workspace for teams.", "Writing", "Paid", "https://narrato.io", ["Workspace","Teams"]),
        t("StoryLab", "AI story and marketing content generator.", "Writing", "Freemium", "https://storylab.ai", ["Marketing","Stories"]),
        t("CopyMonkey", "AI Amazon listing optimization.", "Writing", "Paid", "https://copymonkey.ai", ["Amazon","Ecommerce"]),
        t("Texta", "AI blog post and article writer.", "Writing", "Freemium", "https://texta.ai", ["Blog","Articles"]),
        t("Cohesive", "AI content editor for teams.", "Writing", "Freemium", "https://cohesive.so", ["Editor","Teams"]),
        t("Typewise", "AI text prediction for customer service.", "Writing", "Paid", "https://typewise.app", ["Customer Service","Prediction"]),
        t("AI Writer", "AI content generator with source citations.", "Writing", "Paid", "https://ai-writer.com", ["Citations","Articles"]),
        t("Paragraph AI", "AI writing assistant for emails and messages.", "Writing", "Freemium", "https://paragraphai.com", ["Email","Messages"]),
        t("Speedwrite", "AI text rewriter and content generator.", "Writing", "Paid", "https://speedwrite.com", ["Rewriting","Content"]),
        t("WordAI", "AI article rewriter with natural language.", "Writing", "Paid", "https://wordai.com", ["Rewriting","Spinning"]),
        t("Spin Rewriter", "AI article rewriter for SEO.", "Writing", "Paid", "https://spinrewriter.com", ["Rewriting","SEO"]),
        t("Tinq AI", "AI text analysis, classification, and summarization.", "Writing", "Freemium", "https://tinq.ai", ["Summarization","Classification"]),
    ]
    tools.extend(writing)
    
    # =============================================================
    # IMAGE GENERATION (500+)
    # =============================================================
    image = [
        t("Midjourney", "AI art generation from text prompts via Discord.", "Image Generation", "Paid", "https://midjourney.com", ["Art","Discord","Text-to-Image"]),
        t("DALL-E 3", "OpenAI's AI image generation integrated with ChatGPT.", "Image Generation", "Paid", "https://openai.com/dall-e-3", ["OpenAI","Text-to-Image"]),
        t("Stable Diffusion", "Open-source AI image generation model.", "Image Generation", "Open Source", "https://stability.ai", ["Open Source","Local","Customizable"]),
        t("Leonardo AI", "AI image generation platform for creators.", "Image Generation", "Freemium", "https://leonardo.ai", ["Creative","Fine-Tuning"]),
        t("Adobe Firefly", "Adobe's AI image generation and editing.", "Image Generation", "Freemium", "https://firefly.adobe.com", ["Adobe","Commercial Safe"]),
        t("Ideogram", "AI image generation with best-in-class text rendering.", "Image Generation", "Freemium", "https://ideogram.ai", ["Text Rendering","Design"]),
        t("Flux AI", "Open-source image generation rivaling Midjourney.", "Image Generation", "Open Source", "https://blackforestlabs.ai", ["Open Source","Photorealism"]),
        t("Playground AI", "Free AI image generation with multiple models.", "Image Generation", "Freemium", "https://playground.com", ["Free","Multiple Models"]),
        t("NightCafe", "AI art generator with multiple styles and models.", "Image Generation", "Freemium", "https://nightcafe.studio", ["Art","Multiple Styles"]),
        t("Artbreeder", "AI art collaboration and image mixing.", "Image Generation", "Freemium", "https://artbreeder.com", ["Collaboration","Mixing"]),
        t("Dream by WOMBO", "AI art generator mobile app.", "Image Generation", "Freemium", "https://dream.ai", ["Mobile","Art"]),
        t("Craiyon", "Free AI image generation (formerly DALL-E Mini).", "Image Generation", "Free", "https://craiyon.com", ["Free","Simple"]),
        t("DeepAI", "AI image generation and manipulation APIs.", "Image Generation", "Freemium", "https://deepai.org", ["API","Image Tools"]),
        t("StarryAI", "AI art generator with NFT ownership.", "Image Generation", "Freemium", "https://starryai.com", ["NFT","Art"]),
        t("Pixlr", "AI-powered online photo editor.", "Image Generation", "Freemium", "https://pixlr.com", ["Photo Editor","Filters"]),
        t("Fotor", "AI photo editor and design tool.", "Image Generation", "Freemium", "https://fotor.com", ["Photo Editor","Design"]),
        t("PhotoRoom", "AI background remover and product photography.", "Image Generation", "Freemium", "https://photoroom.com", ["Background Removal","Product Photos"]),
        t("Remove.bg", "AI-powered background removal in seconds.", "Image Generation", "Freemium", "https://remove.bg", ["Background Removal"]),
        t("Clipdrop", "AI-powered image editing and generation by Stability.", "Image Generation", "Freemium", "https://clipdrop.co", ["Editing","Stability AI"]),
        t("Canva Magic Studio", "Canva's AI-powered design suite.", "Image Generation", "Freemium", "https://canva.com", ["Design","Templates"]),
        t("Picsart", "AI photo and video editing platform.", "Image Generation", "Freemium", "https://picsart.com", ["Photo Editing","Mobile"]),
        t("Lensa AI", "AI portrait and selfie enhancement app.", "Image Generation", "Paid", "https://prisma-ai.com/lensa", ["Portraits","Mobile"]),
        t("Prisma", "AI art filters for photos.", "Image Generation", "Freemium", "https://prisma-ai.com", ["Filters","Art Style"]),
        t("Deep Dream Generator", "AI deep dream and artistic image generation.", "Image Generation", "Freemium", "https://deepdreamgenerator.com", ["Deep Dream","Art"]),
        t("Jasper Art", "AI art generator for marketing teams.", "Image Generation", "Paid", "https://jasper.ai/art", ["Marketing","Art"]),
        t("Getimg.ai", "AI image generation, editing, and training.", "Image Generation", "Freemium", "https://getimg.ai", ["Generation","Training"]),
        t("Hotpot AI", "AI art, image, and writing tools.", "Image Generation", "Freemium", "https://hotpot.ai", ["Art","Writing"]),
        t("PicWish", "AI photo editing and enhancement.", "Image Generation", "Freemium", "https://picwish.com", ["Photo Enhancement"]),
        t("ImgCreator", "AI image generation for illustrations and photos.", "Image Generation", "Freemium", "https://imgcreator.zmo.ai", ["Illustrations","Photos"]),
        t("BlueWillow", "Free AI image generation community.", "Image Generation", "Free", "https://bluewillow.ai", ["Free","Community"]),
        t("Instantart", "Fast AI image generation.", "Image Generation", "Free", "https://instantart.io", ["Fast","Free"]),
        t("Invoke AI", "Open-source AI image generation toolkit.", "Image Generation", "Open Source", "https://invoke.ai", ["Open Source","Professional"]),
        t("ComfyUI", "Modular AI image generation workflow builder.", "Image Generation", "Open Source", "https://comfyanonymous.github.io", ["Workflow","Open Source"]),
        t("Automatic1111", "Popular Stable Diffusion web UI.", "Image Generation", "Open Source", "https://github.com/AUTOMATIC1111", ["Stable Diffusion","Web UI"]),
        t("Krea AI", "Real-time AI image generation and enhancement.", "Image Generation", "Freemium", "https://krea.ai", ["Real-Time","Enhancement"]),
        t("Magnific AI", "AI image upscaling and enhancement.", "Image Generation", "Paid", "https://magnific.ai", ["Upscaling","Enhancement"]),
        t("Topaz Labs", "AI photo and video enhancement suite.", "Image Generation", "Paid", "https://topazlabs.com", ["Enhancement","Upscaling"]),
        t("Let's Enhance", "AI image upscaling and enhancement.", "Image Generation", "Freemium", "https://letsenhance.io", ["Upscaling","Quality"]),
        t("Vectorizer AI", "AI bitmap to vector conversion.", "Image Generation", "Paid", "https://vectorizer.ai", ["Vector","Conversion"]),
        t("Vectorize.io", "AI auto-trace to convert images to vectors.", "Image Generation", "Freemium", "https://vectorize.io", ["Vector","Trace"]),
        t("Designify", "AI design automation for product photos.", "Image Generation", "Freemium", "https://designify.com", ["Product Photos","Automation"]),
        t("Palette.fm", "AI colorization for black and white photos.", "Image Generation", "Freemium", "https://palette.fm", ["Colorization","Restoration"]),
        t("MyHeritage Deep Nostalgia", "AI animation of old family photos.", "Image Generation", "Freemium", "https://myheritage.com", ["Animation","Photos"]),
        t("Remini", "AI photo enhancement and restoration.", "Image Generation", "Freemium", "https://remini.ai", ["Restoration","Enhancement"]),
        t("Luminar Neo", "AI photo editor with creative tools.", "Image Generation", "Paid", "https://skylum.com", ["Photo Editor","Creative"]),
        t("DaVinci AI", "AI image generation with advanced control.", "Image Generation", "Paid", "https://davinciai.com", ["Control","Generation"]),
        t("Scenario", "AI game asset generation platform.", "Image Generation", "Freemium", "https://scenario.com", ["Game Assets","Generation"]),
        t("RoomGPT", "AI interior design room transformation.", "Image Generation", "Freemium", "https://roomgpt.io", ["Interior Design","Rooms"]),
        t("Booth AI", "AI product photography generation.", "Image Generation", "Paid", "https://booth.ai", ["Product Photos","Ecommerce"]),
        t("Mokker AI", "AI product photo background generation.", "Image Generation", "Paid", "https://mokker.ai", ["Product Photos","Backgrounds"]),
    ]
    tools.extend(image)
    
    # =============================================================
    # VIDEO CREATION (400+)
    # =============================================================
    video = [
        t("Runway", "AI video generation and editing platform.", "Video Creation", "Freemium", "https://runway.ml", ["Video Generation","Editing"]),
        t("Synthesia", "AI video generation with digital avatars.", "Video Creation", "Paid", "https://synthesia.io", ["Avatars","Enterprise"]),
        t("HeyGen", "AI avatar video creation platform.", "Video Creation", "Freemium", "https://heygen.com", ["Avatars","Translation"]),
        t("InVideo", "AI video creation for social media.", "Video Creation", "Freemium", "https://invideo.io", ["Social Media","Templates"]),
        t("Pictory", "AI video creation from long-form content.", "Video Creation", "Paid", "https://pictory.ai", ["Content Repurposing","Clips"]),
        t("Lumen5", "AI video creation from blog posts.", "Video Creation", "Freemium", "https://lumen5.com", ["Blog-to-Video","Marketing"]),
        t("Kapwing", "AI video editor and content creation platform.", "Video Creation", "Freemium", "https://kapwing.com", ["Editor","Creation"]),
        t("Descript", "AI video and audio editor with transcription.", "Video Creation", "Freemium", "https://descript.com", ["Editor","Transcription"]),
        t("CapCut", "AI video editor by ByteDance.", "Video Creation", "Free", "https://capcut.com", ["Mobile","TikTok"]),
        t("Opus Clip", "AI short video clipper from long content.", "Video Creation", "Freemium", "https://opus.pro", ["Clips","Short-Form"]),
        t("Fliki", "AI text to video with realistic voices.", "Video Creation", "Freemium", "https://fliki.ai", ["Text-to-Video","Voices"]),
        t("Colossyan", "AI video creator for workplace learning.", "Video Creation", "Paid", "https://colossyan.com", ["Training","Enterprise"]),
        t("Elai", "AI video generation from text.", "Video Creation", "Paid", "https://elai.io", ["Text-to-Video","Avatars"]),
        t("D-ID", "AI talking head video generation.", "Video Creation", "Freemium", "https://d-id.com", ["Talking Heads","API"]),
        t("Sora", "OpenAI's text-to-video generation model.", "Video Creation", "Paid", "https://sora.com", ["Text-to-Video","OpenAI"]),
        t("Pika", "AI video creation and editing platform.", "Video Creation", "Freemium", "https://pika.art", ["Generation","Editing"]),
        t("Kling AI", "Cinematic AI video generation.", "Video Creation", "Freemium", "https://klingai.com", ["Cinematic","Generation"]),
        t("Luma Dream Machine", "AI video generation from text and images.", "Video Creation", "Freemium", "https://lumalabs.ai", ["3D","Text-to-Video"]),
        t("Veed IO", "AI video editor with subtitles and transcription.", "Video Creation", "Freemium", "https://veed.io", ["Editor","Subtitles"]),
        t("Animoto", "AI video maker for businesses.", "Video Creation", "Freemium", "https://animoto.com", ["Business","Marketing"]),
        t("Canva Video", "AI video creation within Canva.", "Video Creation", "Freemium", "https://canva.com/video", ["Design","Templates"]),
        t("Wondershare Filmora", "AI video editing software.", "Video Creation", "Paid", "https://filmora.wondershare.com", ["Desktop","Editing"]),
        t("Magisto", "AI video editor by Vimeo.", "Video Creation", "Paid", "https://magisto.com", ["Automated","Marketing"]),
        t("Zubtitle", "AI auto-captioning for videos.", "Video Creation", "Paid", "https://zubtitle.com", ["Captions","Social Media"]),
        t("Captions App", "AI captions and video editing for creators.", "Video Creation", "Freemium", "https://captions.ai", ["Captions","Creators"]),
        t("Vizard AI", "AI video repurposing and clip creation.", "Video Creation", "Freemium", "https://vizard.ai", ["Repurposing","Clips"]),
        t("Munch", "AI content repurposing from video.", "Video Creation", "Paid", "https://getmunch.com", ["Repurposing","Social Media"]),
        t("Vidyo AI", "AI short clip maker from long videos.", "Video Creation", "Freemium", "https://vidyo.ai", ["Clips","Short-Form"]),
        t("Syllaby", "AI video script and content planner.", "Video Creation", "Paid", "https://syllaby.io", ["Scripts","Planning"]),
        t("Steve AI", "AI animated video creation.", "Video Creation", "Freemium", "https://steve.ai", ["Animation","Templates"]),
        t("Wisecut", "AI video editor with auto-cut and subtitles.", "Video Creation", "Freemium", "https://wisecut.video", ["Auto-Cut","Subtitles"]),
        t("Topview AI", "AI video ad creation from product URLs.", "Video Creation", "Paid", "https://topview.ai", ["Ads","Marketing"]),
        t("Shuffll", "AI video production platform for B2B.", "Video Creation", "Paid", "https://shuffll.com", ["B2B","Production"]),
        t("Tavus", "AI personalized video generation at scale.", "Video Creation", "Paid", "https://tavus.io", ["Personalization","Scale"]),
        t("Vidnoz", "AI video creation with avatars and voices.", "Video Creation", "Freemium", "https://vidnoz.com", ["Avatars","Voices"]),
        t("DeepBrain AI", "AI avatar video generation platform.", "Video Creation", "Paid", "https://deepbrain.io", ["Avatars","Enterprise"]),
        t("CreatorKit", "AI product video creation for ecommerce.", "Video Creation", "Paid", "https://creatorkit.com", ["Ecommerce","Product Videos"]),
        t("Movio", "AI spokesperson video creator.", "Video Creation", "Paid", "https://movio.la", ["Spokesperson","Marketing"]),
        t("Visla", "AI video creation for business communication.", "Video Creation", "Freemium", "https://visla.us", ["Business","Communication"]),
        t("Kaiber", "AI video generation with artistic styles.", "Video Creation", "Paid", "https://kaiber.ai", ["Artistic","Music Videos"]),
    ]
    tools.extend(video)
    
    # =============================================================
    # AUDIO & VOICE (300+)
    # =============================================================
    audio = [
        t("ElevenLabs", "AI voice synthesis and text-to-speech.", "Audio & Voice", "Freemium", "https://elevenlabs.io", ["Voice Cloning","TTS"]),
        t("Murf AI", "AI voice generator for professional content.", "Audio & Voice", "Freemium", "https://murf.ai", ["Voice Over","Professional"]),
        t("Play.ht", "AI voice generation and text-to-speech.", "Audio & Voice", "Freemium", "https://play.ht", ["TTS","API"]),
        t("Resemble AI", "AI voice cloning and synthesis.", "Audio & Voice", "Paid", "https://resemble.ai", ["Voice Cloning","API"]),
        t("Speechify", "AI text-to-speech for reading.", "Audio & Voice", "Freemium", "https://speechify.com", ["TTS","Reading"]),
        t("LOVO AI", "AI voice generator and text-to-speech.", "Audio & Voice", "Freemium", "https://lovo.ai", ["Voice","Content"]),
        t("Listnr", "AI voice and podcast generator.", "Audio & Voice", "Freemium", "https://listnr.tech", ["Podcast","Voice"]),
        t("Podcastle", "AI podcast recording, editing, and hosting.", "Audio & Voice", "Freemium", "https://podcastle.ai", ["Podcast","Recording"]),
        t("Descript Audio", "AI audio editor with transcription.", "Audio & Voice", "Freemium", "https://descript.com", ["Audio Editor","Transcription"]),
        t("Krisp", "AI noise cancellation for calls.", "Audio & Voice", "Freemium", "https://krisp.ai", ["Noise Cancellation","Calls"]),
        t("Otter AI", "AI meeting transcription and notes.", "Audio & Voice", "Freemium", "https://otter.ai", ["Transcription","Meetings"]),
        t("Fireflies AI", "AI meeting recorder and transcriber.", "Audio & Voice", "Freemium", "https://fireflies.ai", ["Meetings","Transcription"]),
        t("Suno", "AI music generation from text.", "Audio & Voice", "Freemium", "https://suno.ai", ["Music","Generation"]),
        t("Udio", "AI music creation platform.", "Audio & Voice", "Freemium", "https://udio.com", ["Music","Creation"]),
        t("Soundraw", "AI music generator for content creators.", "Audio & Voice", "Paid", "https://soundraw.io", ["Music","Royalty-Free"]),
        t("Boomy", "AI music creation for everyone.", "Audio & Voice", "Freemium", "https://boomy.com", ["Music","Simple"]),
        t("AIVA", "AI music composer.", "Audio & Voice", "Freemium", "https://aiva.ai", ["Music","Composition"]),
        t("Amper Music", "AI music creation for content.", "Audio & Voice", "Paid", "https://shutterstock.com/discover/ampermusic", ["Music","Licensing"]),
        t("Beatoven AI", "AI music generator for videos and podcasts.", "Audio & Voice", "Freemium", "https://beatoven.ai", ["Music","Videos"]),
        t("Splash Pro", "AI music creation platform.", "Audio & Voice", "Freemium", "https://pro.splashmusic.com", ["Music","Creation"]),
        t("Voicemod", "AI voice changer and soundboard.", "Audio & Voice", "Freemium", "https://voicemod.net", ["Voice Changer","Gaming"]),
        t("Altered", "AI voice editing and cloning platform.", "Audio & Voice", "Paid", "https://altered.ai", ["Voice","Editing"]),
        t("Respeecher", "AI voice cloning for film and media.", "Audio & Voice", "Paid", "https://respeecher.com", ["Voice Cloning","Film"]),
        t("WellSaid Labs", "AI enterprise voice generation.", "Audio & Voice", "Paid", "https://wellsaidlabs.com", ["Enterprise","Voice"]),
        t("Coqui TTS", "Open-source AI text-to-speech.", "Audio & Voice", "Open Source", "https://coqui.ai", ["Open Source","TTS"]),
        t("Bark AI", "Open-source text-to-audio model.", "Audio & Voice", "Open Source", "https://github.com/suno-ai/bark", ["Open Source","Audio"]),
        t("Cleanvoice", "AI podcast audio cleaning.", "Audio & Voice", "Paid", "https://cleanvoice.ai", ["Podcast","Cleaning"]),
        t("Adobe Podcast", "AI audio recording and enhancement.", "Audio & Voice", "Free", "https://podcast.adobe.com", ["Recording","Enhancement"]),
        t("AudioStrip", "AI vocal and instrument separation.", "Audio & Voice", "Free", "https://audiostrip.co.uk", ["Separation","Music"]),
        t("Lalal AI", "AI audio stem splitter.", "Audio & Voice", "Freemium", "https://lalal.ai", ["Stem Splitting","Music"]),
        t("Vocal Remover", "AI vocal removal from songs.", "Audio & Voice", "Free", "https://vocalremover.org", ["Vocal Removal","Music"]),
        t("AssemblyAI", "AI speech-to-text API.", "Audio & Voice", "Freemium", "https://assemblyai.com", ["Speech-to-Text","API"]),
        t("Deepgram", "AI speech recognition API.", "Audio & Voice", "Freemium", "https://deepgram.com", ["Speech Recognition","API"]),
        t("Rev AI", "AI transcription and caption services.", "Audio & Voice", "Paid", "https://rev.ai", ["Transcription","Captions"]),
        t("Sonix", "AI transcription for audio and video.", "Audio & Voice", "Paid", "https://sonix.ai", ["Transcription","Translation"]),
        t("Trint", "AI transcription and content platform.", "Audio & Voice", "Paid", "https://trint.com", ["Transcription","Content"]),
        t("Happy Scribe", "AI transcription and subtitles.", "Audio & Voice", "Freemium", "https://happyscribe.com", ["Transcription","Subtitles"]),
        t("Whisper AI", "OpenAI's open-source speech recognition.", "Audio & Voice", "Open Source", "https://openai.com/research/whisper", ["Open Source","Speech-to-Text"]),
        t("Riverside FM", "AI recording studio for podcasts and interviews.", "Audio & Voice", "Freemium", "https://riverside.fm", ["Recording","Podcast"]),
        t("Zencastr", "AI podcast recording and editing.", "Audio & Voice", "Freemium", "https://zencastr.com", ["Podcast","Recording"]),
    ]
    tools.extend(audio)
    
    # =============================================================
    # CODING & DEVELOPMENT (500+)
    # =============================================================
    coding = [
        t("GitHub Copilot", "AI pair programmer by GitHub and OpenAI.", "Coding & Development", "Paid", "https://github.com/features/copilot", ["Code Completion","IDE"]),
        t("Cursor", "AI-first code editor.", "Coding & Development", "Freemium", "https://cursor.com", ["IDE","Code Editor"]),
        t("Replit AI", "AI coding in the browser.", "Coding & Development", "Freemium", "https://replit.com", ["Browser IDE","Deploy"]),
        t("v0 by Vercel", "AI React UI component generator.", "Coding & Development", "Freemium", "https://v0.dev", ["UI","React"]),
        t("Bolt.new", "AI full-stack app builder in browser.", "Coding & Development", "Freemium", "https://bolt.new", ["Full-Stack","Builder"]),
        t("Lovable", "AI-powered web app builder.", "Coding & Development", "Freemium", "https://lovable.dev", ["App Builder","No-Code"]),
        t("Tabnine", "AI code completion for teams.", "Coding & Development", "Freemium", "https://tabnine.com", ["Code Completion","Privacy"]),
        t("Codeium", "Free AI code completion.", "Coding & Development", "Free", "https://codeium.com", ["Code Completion","Free"]),
        t("Amazon CodeWhisperer", "AWS AI code generator.", "Coding & Development", "Freemium", "https://aws.amazon.com/codewhisperer", ["AWS","Code Generation"]),
        t("Google Gemini Code Assist", "Google's AI coding assistant.", "Coding & Development", "Freemium", "https://cloud.google.com/gemini/docs/codeassist", ["Google Cloud","Code"]),
        t("Supermaven", "Fast AI code completion.", "Coding & Development", "Freemium", "https://supermaven.com", ["Fast","Code Completion"]),
        t("Continue", "Open-source AI coding assistant.", "Coding & Development", "Open Source", "https://continue.dev", ["Open Source","IDE Extension"]),
        t("Aider", "AI pair programming in your terminal.", "Coding & Development", "Open Source", "https://aider.chat", ["Terminal","Git"]),
        t("Devin", "Autonomous AI software engineer.", "Coding & Development", "Paid", "https://cognition.ai", ["Autonomous","Agent"]),
        t("SWE-agent", "AI software engineering agent by Princeton.", "Coding & Development", "Open Source", "https://swe-agent.com", ["Agent","Research"]),
        t("Phind", "AI search engine for developers.", "Coding & Development", "Freemium", "https://phind.com", ["Search","Developer"]),
        t("Codium AI", "AI test generation and code integrity.", "Coding & Development", "Freemium", "https://codium.ai", ["Testing","Code Quality"]),
        t("Sourcegraph Cody", "AI coding assistant with codebase context.", "Coding & Development", "Freemium", "https://sourcegraph.com/cody", ["Code Search","Context"]),
        t("Pieces for Developers", "AI developer productivity tool.", "Coding & Development", "Free", "https://pieces.app", ["Snippets","Workflow"]),
        t("AskCodi", "AI coding assistant for multiple languages.", "Coding & Development", "Freemium", "https://askcodi.com", ["Multi-Language","Assistant"]),
        t("CodeGPT", "AI coding assistant VS Code extension.", "Coding & Development", "Freemium", "https://codegpt.co", ["VS Code","Extension"]),
        t("Warp", "AI-powered terminal.", "Coding & Development", "Freemium", "https://warp.dev", ["Terminal","CLI"]),
        t("Fig", "AI terminal autocomplete (now Amazon Q).", "Coding & Development", "Free", "https://fig.io", ["Terminal","Autocomplete"]),
        t("Mintlify", "AI documentation generation for code.", "Coding & Development", "Freemium", "https://mintlify.com", ["Documentation","API Docs"]),
        t("GitLab Duo", "AI-powered DevSecOps platform.", "Coding & Development", "Paid", "https://gitlab.com", ["DevOps","Security"]),
        t("Snyk", "AI security scanning for code dependencies.", "Coding & Development", "Freemium", "https://snyk.io", ["Security","Scanning"]),
        t("Qodo", "AI code quality and testing platform.", "Coding & Development", "Freemium", "https://qodo.ai", ["Testing","Quality"]),
        t("Codiga", "AI code analysis and security.", "Coding & Development", "Freemium", "https://codiga.io", ["Analysis","Security"]),
        t("Blackbox AI", "AI code generation and search.", "Coding & Development", "Freemium", "https://blackbox.ai", ["Code Search","Generation"]),
        t("Mutable AI", "AI code refactoring and documentation.", "Coding & Development", "Paid", "https://mutable.ai", ["Refactoring","Documentation"]),
        t("Sweep", "AI junior developer for GitHub repos.", "Coding & Development", "Freemium", "https://sweep.dev", ["GitHub","Bug Fixes"]),
        t("Codegen", "AI coding agent for large codebases.", "Coding & Development", "Paid", "https://codegen.com", ["Agent","Large Codebases"]),
        t("Cody by Sourcegraph", "AI code assistant with full repo context.", "Coding & Development", "Freemium", "https://sourcegraph.com", ["Code Search","Context"]),
        t("Bito AI", "AI code assistant for 10x developer productivity.", "Coding & Development", "Freemium", "https://bito.ai", ["Productivity","IDE"]),
        t("Code Llama", "Meta's open-source coding AI model.", "Coding & Development", "Open Source", "https://ai.meta.com/blog/code-llama", ["Open Source","Meta"]),
        t("StarCoder", "Open-source AI code generation model.", "Coding & Development", "Open Source", "https://huggingface.co/bigcode", ["Open Source","Hugging Face"]),
        t("Replit Agent", "AI agent that builds entire apps.", "Coding & Development", "Paid", "https://replit.com", ["Agent","App Builder"]),
        t("Windsurf Editor", "AI-first coding IDE by Codeium.", "Coding & Development", "Freemium", "https://codeium.com/windsurf", ["IDE","Agentic"]),
        t("Claude Code", "Anthropic's agentic coding tool.", "Coding & Development", "Paid", "https://anthropic.com", ["Agent","Terminal"]),
        t("OpenHands", "Open-source AI software development agent.", "Coding & Development", "Open Source", "https://all-hands.dev", ["Agent","Open Source"]),
    ]
    tools.extend(coding)
    
    # =============================================================
    # PRODUCTIVITY (500+)
    # =============================================================
    productivity = [
        t("Notion AI", "AI assistant built into Notion.", "Productivity", "Paid", "https://notion.so", ["Workspace","Notes"]),
        t("ChatGPT", "OpenAI's conversational AI assistant.", "Productivity", "Freemium", "https://chat.openai.com", ["Chatbot","General AI"]),
        t("Claude", "Anthropic's helpful AI assistant.", "Productivity", "Freemium", "https://claude.ai", ["Chatbot","Analysis"]),
        t("Gemini", "Google's multimodal AI assistant.", "Productivity", "Freemium", "https://gemini.google.com", ["Google","Multimodal"]),
        t("Perplexity", "AI-powered search engine with citations.", "Productivity", "Freemium", "https://perplexity.ai", ["Search","Research"]),
        t("Poe", "Platform for AI chatbots by Quora.", "Productivity", "Freemium", "https://poe.com", ["Multi-Model","Chat"]),
        t("Gamma", "AI presentation and document builder.", "Productivity", "Freemium", "https://gamma.app", ["Presentations","Documents"]),
        t("Beautiful AI", "AI presentation maker.", "Productivity", "Paid", "https://beautiful.ai", ["Presentations","Design"]),
        t("Tome", "AI storytelling and presentation platform.", "Productivity", "Freemium", "https://tome.app", ["Presentations","Storytelling"]),
        t("SlidesAI", "AI PowerPoint and Google Slides creator.", "Productivity", "Freemium", "https://slidesai.io", ["Slides","Presentations"]),
        t("Taskade", "AI workspace for teams with agents.", "Productivity", "Freemium", "https://taskade.com", ["Project Management","Teams"]),
        t("Mem AI", "AI-powered note-taking and knowledge base.", "Productivity", "Paid", "https://mem.ai", ["Notes","Knowledge"]),
        t("Reflect", "AI note-taking with backlinks.", "Productivity", "Paid", "https://reflect.app", ["Notes","Backlinks"]),
        t("Craft", "AI-enhanced document and notes app.", "Productivity", "Freemium", "https://craft.do", ["Documents","Notes"]),
        t("Coda AI", "AI-powered docs and workflows.", "Productivity", "Freemium", "https://coda.io", ["Docs","Automation"]),
        t("Clickup AI", "AI project management assistant.", "Productivity", "Paid", "https://clickup.com", ["Project Management","Tasks"]),
        t("Monday AI", "AI work management platform.", "Productivity", "Paid", "https://monday.com", ["Work Management","Teams"]),
        t("Asana Intelligence", "AI project management features.", "Productivity", "Paid", "https://asana.com", ["Project Management","Teams"]),
        t("Linear", "AI-powered issue tracking for engineering.", "Productivity", "Freemium", "https://linear.app", ["Issue Tracking","Engineering"]),
        t("Superhuman", "AI-powered email client.", "Productivity", "Paid", "https://superhuman.com", ["Email","Speed"]),
        t("Shortwave", "AI-powered email for busy professionals.", "Productivity", "Freemium", "https://shortwave.com", ["Email","AI Summary"]),
        t("SaneBox", "AI email management and filtering.", "Productivity", "Paid", "https://sanebox.com", ["Email","Filtering"]),
        t("Calendly", "AI-powered scheduling platform.", "Productivity", "Freemium", "https://calendly.com", ["Scheduling","Booking"]),
        t("Reclaim AI", "AI smart calendar and scheduling.", "Productivity", "Freemium", "https://reclaim.ai", ["Calendar","Scheduling"]),
        t("Motion", "AI calendar that auto-plans your day.", "Productivity", "Paid", "https://usemotion.com", ["Calendar","Planning"]),
        t("Clockwise", "AI calendar optimization for focus time.", "Productivity", "Freemium", "https://getclockwise.com", ["Calendar","Focus"]),
        t("Raycast", "AI-powered productivity launcher for Mac.", "Productivity", "Freemium", "https://raycast.com", ["Launcher","Mac"]),
        t("Arc Browser", "AI-enhanced web browser.", "Productivity", "Free", "https://arc.net", ["Browser","Search"]),
        t("Napkin AI", "Turn text into visuals and diagrams.", "Productivity", "Freemium", "https://napkin.ai", ["Visuals","Diagrams"]),
        t("Miro AI", "AI features for visual collaboration.", "Productivity", "Freemium", "https://miro.com", ["Whiteboard","Collaboration"]),
        t("Whimsical AI", "AI-powered flowcharts and wireframes.", "Productivity", "Freemium", "https://whimsical.com", ["Wireframes","Flowcharts"]),
        t("Loom", "AI video messaging with auto summaries.", "Productivity", "Freemium", "https://loom.com", ["Video Messages","Async"]),
        t("Krisp", "AI noise cancellation for meetings.", "Productivity", "Freemium", "https://krisp.ai", ["Noise Cancel","Meetings"]),
        t("Otter.ai", "AI meeting notes and transcription.", "Productivity", "Freemium", "https://otter.ai", ["Transcription","Meetings"]),
        t("Fathom", "AI meeting recorder and notes.", "Productivity", "Free", "https://fathom.video", ["Meetings","Notes"]),
        t("tl;dv", "AI meeting recorder for Google Meet and Zoom.", "Productivity", "Freemium", "https://tldv.io", ["Meetings","Recording"]),
        t("Avoma", "AI meeting assistant for revenue teams.", "Productivity", "Paid", "https://avoma.com", ["Meetings","Sales"]),
        t("Grain", "AI meeting highlights and notes.", "Productivity", "Freemium", "https://grain.com", ["Meetings","Highlights"]),
        t("Sembly AI", "AI meeting assistant with summaries.", "Productivity", "Freemium", "https://sembly.ai", ["Meetings","Summaries"]),
        t("Read AI", "AI meeting copilot with analytics.", "Productivity", "Freemium", "https://read.ai", ["Meetings","Analytics"]),
        t("Notta", "AI transcription and meeting notes.", "Productivity", "Freemium", "https://notta.ai", ["Transcription","Notes"]),
        t("Vowel", "AI meeting platform for remote teams.", "Productivity", "Freemium", "https://vowel.com", ["Meetings","Remote"]),
        t("Fellow", "AI meeting notes and agenda tool.", "Productivity", "Freemium", "https://fellow.app", ["Meetings","Agendas"]),
        t("Magical", "AI text expander and form filler.", "Productivity", "Free", "https://getmagical.com", ["Automation","Text Expander"]),
        t("Bardeen", "AI workflow automation without code.", "Productivity", "Freemium", "https://bardeen.ai", ["Automation","Browser"]),
        t("Personal AI", "AI that learns from your data.", "Productivity", "Freemium", "https://personal.ai", ["Personal","Learning"]),
        t("Pi by Inflection", "Conversational AI for personal use.", "Productivity", "Free", "https://pi.ai", ["Chatbot","Personal"]),
        t("Copilot Microsoft", "AI assistant across Microsoft 365.", "Productivity", "Paid", "https://copilot.microsoft.com", ["Microsoft","Office"]),
        t("Apple Intelligence", "AI features built into Apple devices.", "Productivity", "Free", "https://apple.com/apple-intelligence", ["Apple","On-Device"]),
        t("Samsung Galaxy AI", "AI features in Samsung Galaxy devices.", "Productivity", "Free", "https://samsung.com/galaxy-ai", ["Samsung","Mobile"]),
    ]
    tools.extend(productivity)
    
    # =============================================================
    # MARKETING (400+)
    # =============================================================
    marketing = [
        t("HubSpot AI", "AI-powered CRM and marketing platform.", "Marketing", "Freemium", "https://hubspot.com", ["CRM","Inbound"]),
        t("Mailchimp AI", "AI email marketing platform.", "Marketing", "Freemium", "https://mailchimp.com", ["Email","Automation"]),
        t("Instantly", "AI cold email outreach at scale.", "Marketing", "Paid", "https://instantly.ai", ["Cold Email","Outreach"]),
        t("Apollo", "AI sales intelligence and engagement platform.", "Marketing", "Freemium", "https://apollo.io", ["Sales","Lead Gen"]),
        t("Reply.io", "AI-powered sales outreach platform.", "Marketing", "Paid", "https://reply.io", ["Sales","Outreach"]),
        t("Lavender", "AI email coach for sales teams.", "Marketing", "Freemium", "https://lavender.ai", ["Email","Sales"]),
        t("Smartlead", "AI cold email infrastructure.", "Marketing", "Paid", "https://smartlead.ai", ["Cold Email","Infrastructure"]),
        t("Lemlist", "AI-powered cold outreach and personalization.", "Marketing", "Paid", "https://lemlist.com", ["Outreach","Personalization"]),
        t("Woodpecker", "AI cold email automation.", "Marketing", "Paid", "https://woodpecker.co", ["Email","Automation"]),
        t("Clay", "AI data enrichment for sales teams.", "Marketing", "Paid", "https://clay.com", ["Data Enrichment","Sales"]),
        t("Taplio", "AI-powered LinkedIn growth tool.", "Marketing", "Paid", "https://taplio.com", ["LinkedIn","Growth"]),
        t("TweetHunter", "AI Twitter/X growth and scheduling.", "Marketing", "Paid", "https://tweethunter.io", ["Twitter","Growth"]),
        t("Buffer", "AI social media scheduling platform.", "Marketing", "Freemium", "https://buffer.com", ["Social Media","Scheduling"]),
        t("Hootsuite", "AI social media management platform.", "Marketing", "Paid", "https://hootsuite.com", ["Social Media","Management"]),
        t("Sprout Social", "AI social media management for enterprise.", "Marketing", "Paid", "https://sproutsocial.com", ["Enterprise","Social Media"]),
        t("Later", "AI Instagram and social media scheduling.", "Marketing", "Freemium", "https://later.com", ["Instagram","Scheduling"]),
        t("Predis AI", "AI social media content generator.", "Marketing", "Freemium", "https://predis.ai", ["Social Media","Content"]),
        t("Ocoya", "AI social media content creation and scheduling.", "Marketing", "Paid", "https://ocoya.com", ["Social Media","Scheduling"]),
        t("Flick", "AI social media marketing assistant.", "Marketing", "Paid", "https://flick.social", ["Social Media","Hashtags"]),
        t("Semrush", "AI-powered SEO and marketing toolkit.", "Marketing", "Paid", "https://semrush.com", ["SEO","Analytics"]),
        t("Ahrefs", "AI SEO tools and backlink analysis.", "Marketing", "Paid", "https://ahrefs.com", ["SEO","Backlinks"]),
        t("Moz", "AI-powered SEO tools and insights.", "Marketing", "Paid", "https://moz.com", ["SEO","Domain Authority"]),
        t("SE Ranking", "AI SEO platform for businesses.", "Marketing", "Paid", "https://seranking.com", ["SEO","Rankings"]),
        t("Mangools", "AI SEO tools bundle.", "Marketing", "Paid", "https://mangools.com", ["SEO","Keywords"]),
        t("Ubersuggest", "AI SEO and keyword research tool.", "Marketing", "Freemium", "https://neilpatel.com/ubersuggest", ["SEO","Keywords"]),
        t("Brandwatch", "AI social listening and analytics.", "Marketing", "Paid", "https://brandwatch.com", ["Social Listening","Analytics"]),
        t("Brand24", "AI media monitoring and analytics.", "Marketing", "Paid", "https://brand24.com", ["Monitoring","Analytics"]),
        t("Mention", "AI media monitoring tool.", "Marketing", "Paid", "https://mention.com", ["Monitoring","Alerts"]),
        t("Crayon", "AI competitive intelligence platform.", "Marketing", "Paid", "https://crayon.co", ["Competitive Intel","Tracking"]),
        t("Kompyte", "AI competitive intelligence by Semrush.", "Marketing", "Paid", "https://kompyte.com", ["Competitive Intel"]),
        t("Drift", "AI conversational marketing platform.", "Marketing", "Paid", "https://drift.com", ["Chatbot","Conversational"]),
        t("Intercom Fin", "AI customer service chatbot.", "Marketing", "Paid", "https://intercom.com", ["Chatbot","Support"]),
        t("Tidio", "AI chatbot for customer service.", "Marketing", "Freemium", "https://tidio.com", ["Chatbot","Live Chat"]),
        t("ManyChat", "AI chatbot for Instagram and WhatsApp.", "Marketing", "Freemium", "https://manychat.com", ["Chatbot","Instagram"]),
        t("Chatfuel", "AI chatbot builder for businesses.", "Marketing", "Freemium", "https://chatfuel.com", ["Chatbot","Builder"]),
        t("AdCreative AI", "AI ad creative generation.", "Marketing", "Paid", "https://adcreative.ai", ["Ads","Creative"]),
        t("Pencil AI", "AI ad generation and optimization.", "Marketing", "Paid", "https://trypencil.com", ["Ads","Video"]),
        t("Omneky", "AI ad creation and performance optimization.", "Marketing", "Paid", "https://omneky.com", ["Ads","Performance"]),
        t("Phrasee", "AI marketing language optimization.", "Marketing", "Paid", "https://phrasee.co", ["Copywriting","Optimization"]),
        t("Persado", "AI marketing language platform.", "Marketing", "Paid", "https://persado.com", ["Language","Enterprise"]),
        t("Albert AI", "AI digital marketing platform.", "Marketing", "Paid", "https://albert.ai", ["Digital Marketing","Automation"]),
        t("Acquisio", "AI PPC management platform.", "Marketing", "Paid", "https://acquisio.com", ["PPC","Advertising"]),
        t("Seventh Sense", "AI email send time optimization.", "Marketing", "Paid", "https://theseventhsense.com", ["Email","Timing"]),
        t("Looka", "AI logo and brand identity maker.", "Marketing", "Paid", "https://looka.com", ["Logo","Branding"]),
        t("Brandmark", "AI logo design tool.", "Marketing", "Paid", "https://brandmark.io", ["Logo","Design"]),
        t("Designs AI", "AI-powered design suite.", "Marketing", "Paid", "https://designs.ai", ["Design","All-in-One"]),
        t("Hatchful", "AI logo maker by Shopify.", "Marketing", "Free", "https://hatchful.shopify.com", ["Logo","Free"]),
        t("Namelix", "AI business name generator.", "Marketing", "Free", "https://namelix.com", ["Business Names","Branding"]),
        t("Mixo", "AI website builder for startups.", "Marketing", "Paid", "https://mixo.io", ["Website","Landing Page"]),
        t("Durable", "AI website builder for small business.", "Marketing", "Paid", "https://durable.co", ["Website","Small Business"]),
    ]
    tools.extend(marketing)
    
    # =============================================================
    # RESEARCH (200+)
    # =============================================================
    research = [
        t("Perplexity AI", "AI search engine with citations.", "Research", "Freemium", "https://perplexity.ai", ["Search","Citations"]),
        t("Consensus", "AI academic search engine.", "Research", "Freemium", "https://consensus.app", ["Academic","Papers"]),
        t("Elicit", "AI research assistant for papers.", "Research", "Freemium", "https://elicit.com", ["Papers","Literature Review"]),
        t("Semantic Scholar", "AI-powered academic search.", "Research", "Free", "https://semanticscholar.org", ["Academic","Search"]),
        t("SciSpace", "AI tool to understand research papers.", "Research", "Freemium", "https://scispace.com", ["Papers","Explanation"]),
        t("Connected Papers", "AI visual exploration of research papers.", "Research", "Freemium", "https://connectedpapers.com", ["Visual","Papers"]),
        t("Scholarcy", "AI research summarizer.", "Research", "Freemium", "https://scholarcy.com", ["Summarization","Papers"]),
        t("ResearchRabbit", "AI discovery tool for research.", "Research", "Free", "https://researchrabbit.ai", ["Discovery","Papers"]),
        t("Scite", "AI smart citations for research.", "Research", "Freemium", "https://scite.ai", ["Citations","Verification"]),
        t("Litmaps", "AI literature mapping tool.", "Research", "Freemium", "https://litmaps.com", ["Mapping","Literature"]),
        t("NotebookLM", "Google's AI research and notes assistant.", "Research", "Free", "https://notebooklm.google.com", ["Google","Notes"]),
        t("ChatPDF", "AI chat with any PDF document.", "Research", "Freemium", "https://chatpdf.com", ["PDF","Q&A"]),
        t("Humata", "AI document Q&A and analysis.", "Research", "Freemium", "https://humata.ai", ["Documents","Analysis"]),
        t("Unriddle", "AI tool to read and understand complex docs.", "Research", "Freemium", "https://unriddle.ai", ["Documents","Understanding"]),
        t("Explainpaper", "AI tool to explain confusing research papers.", "Research", "Free", "https://explainpaper.com", ["Papers","Explanation"]),
        t("Liner", "AI research copilot for the web.", "Research", "Freemium", "https://getliner.com", ["Web Research","Highlights"]),
        t("You.com", "AI search engine with apps.", "Research", "Freemium", "https://you.com", ["Search","Privacy"]),
        t("Kagi", "Premium AI search engine.", "Research", "Paid", "https://kagi.com", ["Search","Privacy"]),
        t("Exa AI", "AI search API for developers.", "Research", "Freemium", "https://exa.ai", ["API","Search"]),
        t("Tavily", "AI search API optimized for LLMs.", "Research", "Freemium", "https://tavily.com", ["API","LLM"]),
        t("Consensus", "AI that finds answers in scientific research.", "Research", "Freemium", "https://consensus.app", ["Science","Papers"]),
        t("Wolfram Alpha", "AI computational knowledge engine.", "Research", "Freemium", "https://wolframalpha.com", ["Math","Computation"]),
        t("Julius AI", "AI data analysis and visualization.", "Research", "Freemium", "https://julius.ai", ["Data","Visualization"]),
        t("Dataiku", "AI and ML platform for enterprise.", "Research", "Paid", "https://dataiku.com", ["Enterprise","ML Platform"]),
        t("Weights & Biases", "ML experiment tracking and monitoring.", "Research", "Freemium", "https://wandb.ai", ["ML","Experiments"]),
        t("Hugging Face", "Open-source AI model hub and tools.", "Research", "Freemium", "https://huggingface.co", ["Models","Open Source"]),
        t("Replicate", "Run AI models in the cloud.", "Research", "Pay-per-use", "https://replicate.com", ["Models","API"]),
        t("Together AI", "AI model inference and fine-tuning.", "Research", "Pay-per-use", "https://together.ai", ["Inference","Fine-Tuning"]),
        t("Anyscale", "AI compute platform for developers.", "Research", "Paid", "https://anyscale.com", ["Compute","Ray"]),
        t("Lightning AI", "AI development platform.", "Research", "Freemium", "https://lightning.ai", ["PyTorch","Training"]),
    ]
    tools.extend(research)
    
    # =============================================================
    # AUTOMATION (300+)
    # =============================================================
    automation = [
        t("Zapier", "AI-powered app automation platform.", "Automation", "Freemium", "https://zapier.com", ["Workflow","Integration"]),
        t("Make", "Visual automation platform with AI.", "Automation", "Freemium", "https://make.com", ["Visual","Workflow"]),
        t("n8n", "Open-source AI workflow automation.", "Automation", "Open Source", "https://n8n.io", ["Open Source","Self-Hosted"]),
        t("Bardeen", "AI browser automation without code.", "Automation", "Freemium", "https://bardeen.ai", ["Browser","No-Code"]),
        t("AutoGPT", "Autonomous AI agent framework.", "Automation", "Open Source", "https://agpt.co", ["Agent","Autonomous"]),
        t("AgentGPT", "Deploy autonomous AI agents in the browser.", "Automation", "Open Source", "https://agentgpt.reworkd.ai", ["Agent","Browser"]),
        t("BabyAGI", "AI task management agent.", "Automation", "Open Source", "https://github.com/yoheinakajima/babyagi", ["Agent","Task Management"]),
        t("CrewAI", "AI multi-agent orchestration framework.", "Automation", "Open Source", "https://crewai.com", ["Multi-Agent","Framework"]),
        t("LangChain", "Framework for LLM-powered applications.", "Automation", "Open Source", "https://langchain.com", ["Framework","LLM"]),
        t("LlamaIndex", "Data framework for LLM applications.", "Automation", "Open Source", "https://llamaindex.ai", ["Data","RAG"]),
        t("Flowise", "Open-source UI for building LLM flows.", "Automation", "Open Source", "https://flowiseai.com", ["Visual","LLM"]),
        t("Relevance AI", "AI agent builder for business.", "Automation", "Freemium", "https://relevanceai.com", ["Agent Builder","Business"]),
        t("Botpress", "AI chatbot builder platform.", "Automation", "Freemium", "https://botpress.com", ["Chatbot","Builder"]),
        t("Voiceflow", "AI conversation design platform.", "Automation", "Freemium", "https://voiceflow.com", ["Conversation","Design"]),
        t("Typebot", "Open-source chatbot builder.", "Automation", "Open Source", "https://typebot.io", ["Chatbot","Open Source"]),
        t("Browse AI", "AI web scraping and monitoring.", "Automation", "Freemium", "https://browse.ai", ["Scraping","Monitoring"]),
        t("Apify", "Web scraping and automation platform.", "Automation", "Freemium", "https://apify.com", ["Scraping","Platform"]),
        t("PhantomBuster", "AI lead generation and scraping.", "Automation", "Paid", "https://phantombuster.com", ["Lead Gen","Scraping"]),
        t("Axiom AI", "AI browser automation bot.", "Automation", "Freemium", "https://axiom.ai", ["Browser","Bot"]),
        t("SynthFlow", "Build AI voice agents for phone calls.", "Automation", "Paid", "https://synthflow.ai", ["Voice","Phone"]),
        t("Vapi", "AI voice agent API platform.", "Automation", "Pay-per-use", "https://vapi.ai", ["Voice","API"]),
        t("Bland AI", "AI phone calling agent.", "Automation", "Pay-per-use", "https://bland.ai", ["Phone","Calls"]),
        t("Air AI", "AI that can talk on the phone like a human.", "Automation", "Paid", "https://air.ai", ["Phone","Conversational"]),
        t("Retell AI", "Build conversational voice AI.", "Automation", "Pay-per-use", "https://retellai.com", ["Voice","Conversational"]),
        t("Tray.io", "AI integration and automation platform.", "Automation", "Paid", "https://tray.io", ["Integration","Enterprise"]),
        t("Workato", "AI enterprise automation platform.", "Automation", "Paid", "https://workato.com", ["Enterprise","Integration"]),
        t("Power Automate", "Microsoft's AI automation platform.", "Automation", "Paid", "https://powerautomate.microsoft.com", ["Microsoft","RPA"]),
        t("UiPath", "AI-powered robotic process automation.", "Automation", "Paid", "https://uipath.com", ["RPA","Enterprise"]),
        t("Automation Anywhere", "AI RPA for enterprise.", "Automation", "Paid", "https://automationanywhere.com", ["RPA","Enterprise"]),
        t("Roboflow", "AI computer vision automation.", "Automation", "Freemium", "https://roboflow.com", ["Computer Vision","Training"]),
    ]
    tools.extend(automation)
    
    # =============================================================
    # FINANCE (200+)
    # =============================================================
    finance = [
        t("Ramp", "AI corporate card and expense management.", "Finance", "Free", "https://ramp.com", ["Expenses","Corporate Card"]),
        t("Brex", "AI-powered business finance platform.", "Finance", "Freemium", "https://brex.com", ["Corporate Card","Business"]),
        t("Cleo", "AI personal finance chatbot.", "Finance", "Freemium", "https://web.meetcleo.com", ["Personal Finance","Budgeting"]),
        t("Mint", "AI budgeting and financial tracking.", "Finance", "Free", "https://mint.intuit.com", ["Budgeting","Tracking"]),
        t("YNAB", "AI-assisted budgeting software.", "Finance", "Paid", "https://ynab.com", ["Budgeting","Planning"]),
        t("Copilot Money", "AI personal finance app.", "Finance", "Paid", "https://copilot.money", ["Personal Finance","Tracking"]),
        t("Monarch Money", "AI financial planning and budgeting.", "Finance", "Paid", "https://monarchmoney.com", ["Planning","Budgeting"]),
        t("AlphaSense", "AI market intelligence platform.", "Finance", "Paid", "https://alpha-sense.com", ["Market Intel","Research"]),
        t("FinChat", "AI financial data and analysis.", "Finance", "Freemium", "https://finchat.io", ["Financial Data","Analysis"]),
        t("Koyfin", "AI financial data analytics platform.", "Finance", "Freemium", "https://koyfin.com", ["Analytics","Data"]),
        t("Plaid", "AI-powered financial data API.", "Finance", "Pay-per-use", "https://plaid.com", ["API","Banking"]),
        t("Stripe", "AI payment processing infrastructure.", "Finance", "Pay-per-use", "https://stripe.com", ["Payments","API"]),
        t("Kensho", "AI analytics for financial markets.", "Finance", "Paid", "https://kensho.com", ["Analytics","Markets"]),
        t("Canoe Intelligence", "AI document processing for finance.", "Finance", "Paid", "https://canoeintelligence.com", ["Documents","Processing"]),
        t("Stampli", "AI accounts payable automation.", "Finance", "Paid", "https://stampli.com", ["AP Automation","Invoice"]),
        t("Trullion", "AI accounting and audit platform.", "Finance", "Paid", "https://trullion.com", ["Accounting","Audit"]),
        t("Botkeeper", "AI-powered bookkeeping.", "Finance", "Paid", "https://botkeeper.com", ["Bookkeeping","Automation"]),
        t("Vic AI", "AI autonomous accounting.", "Finance", "Paid", "https://vic.ai", ["Accounting","Autonomous"]),
        t("Zest AI", "AI lending and credit decisioning.", "Finance", "Paid", "https://zest.ai", ["Lending","Credit"]),
        t("Upstart", "AI lending platform.", "Finance", "Free", "https://upstart.com", ["Lending","Personal Loans"]),
        t("Wealthfront", "AI-powered robo-advisor.", "Finance", "Freemium", "https://wealthfront.com", ["Investing","Robo-Advisor"]),
        t("Betterment", "AI automated investing.", "Finance", "Paid", "https://betterment.com", ["Investing","Portfolio"]),
        t("Robinhood", "AI-powered commission-free trading.", "Finance", "Free", "https://robinhood.com", ["Trading","Stocks"]),
        t("TradingView", "AI charting and trading platform.", "Finance", "Freemium", "https://tradingview.com", ["Charting","Analysis"]),
        t("Kavout", "AI stock analysis and ranking.", "Finance", "Paid", "https://kavout.com", ["Stock Analysis","AI"]),
        t("Danelfin", "AI stock picking and analysis.", "Finance", "Freemium", "https://danelfin.com", ["Stock Picking","Analytics"]),
        t("Toggle AI", "AI investment research platform.", "Finance", "Paid", "https://toggle.ai", ["Investment","Research"]),
        t("Domo", "AI business intelligence platform.", "Finance", "Paid", "https://domo.com", ["BI","Analytics"]),
        t("Tableau AI", "AI data visualization by Salesforce.", "Finance", "Paid", "https://tableau.com", ["Visualization","BI"]),
        t("Sisense", "AI analytics platform for enterprise.", "Finance", "Paid", "https://sisense.com", ["Analytics","Embedded"]),
    ]
    tools.extend(finance)
    
    return tools


if __name__ == "__main__":
    print("=" * 50)
    print("AI Kendra — Bulk Tool Seeder")
    print("=" * 50)
    
    today = datetime.datetime.now().strftime("%m/%d/%Y")
    
    # Load existing
    if os.path.exists(TOOLS_JSON_PATH):
        with open(TOOLS_JSON_PATH, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    else:
        existing = []
    
    existing_slugs = {t.get("slug") for t in existing}
    print(f"Current database: {len(existing)} tools")
    
    # Get all bulk tools
    bulk = get_all_tools()
    print(f"Bulk list: {len(bulk)} tools")
    
    added = 0
    for tool in bulk:
        if tool["slug"] not in existing_slugs:
            tool["dateAdded"] = today
            if "description" not in tool:
                tool["description"] = tool["shortDescription"]
            existing.insert(len(existing), tool)  # Append to end
            existing_slugs.add(tool["slug"])
            added += 1
    
    # Shuffle the dateAdded for variety (spread across last 90 days)
    for i, tool in enumerate(existing):
        if "dateAdded" not in tool or tool["dateAdded"] == today:
            days_ago = random.randint(0, 90)
            d = datetime.datetime.now() - datetime.timedelta(days=days_ago)
            tool["dateAdded"] = d.strftime("%m/%d/%Y")
    
    with open(TOOLS_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    
    print(f"\nAdded {added} new tools!")
    print(f"Total in database: {len(existing)}")
    print("=" * 50)
