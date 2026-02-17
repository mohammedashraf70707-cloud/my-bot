import discord
from discord.ext import commands, tasks
import asyncio
import random

# --- الإعدادات (التوكن والـ IDs) ---
TOKEN = 'MTQ3MzEwNTA2MDk3MDg4OTI3OQ.Gnxprv.nP5_XEYVu0z7_XBt9o3iKytkkIHXfLE-3ECJh0'
WASEET_ID = 1193685631705026601 # ID الوسيط حقك
CHANNEL_ID = 1471949497356648570 # ID القناة

# --- قائمة بـ 20 رسالة متنوعة ---
MESSAGES = [
    "أفضل وسيط في العالم وتوسيط سريع",
    "والله أضمن وسيط تعاملت معه في دراقون",
    "تمت عملية التوسيط بنجاح، ثقة وأمان",
    "أنصح الجميع بالتعامل معه، محترم جداً",
    "شكراً لك على المصداقية والسرعة",
    "أفضل تجربة توسيط، ما قصرت بيض الله وجهك",
    "يا شباب اللي يبي وسيط مضمون يروح له",
    "خدمة سريعة وتعامل راقي جداً",
    "تم التوسيط، شكراً على مجهودك الجبار",
    "وسيطنا الغالي شكراً على الأمانة",
    "افضل وسيط تعاملت معه في حياتي والله",
    "ثقة وسرعة ما شاء الله، الله يوفقه",
    "من أفضل الوسطاء اللي مروا علي",
    "تعامل سريع ومصداقية عالية جداً جداً",
    "شكراً على التوسيط السريع والاحترافي",
    "وسيط كفو ويخلصك في ثواني معدودة",
    "الله يعطيك العافية، وسيط ممتاز",
    "أنصح فيه وبشدة، وسيط ثقة 100%",
    "دائماً متألق وسريع في تعامله مع الكل",
    "شكراً يا وحش على أفضل خدمة"
]

# إيموجيات متنوعة عشان الحركة تبين طبيعية
EMOJIS = ["🔥", "✅", "💎", "🤝", "🚀", "✨", "🙏", "👍", "👑", "⭐", "💙", "⚡"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

bot.current_msg_index = 0

@tasks.loop(minutes=5.0) # يرسل رسالة "واحدة" كل 5 دقائق
async def auto_vouch():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        # هنا السحر: ندمج المنشن مع الكلام مع الإيموجي
        base_msg = MESSAGES[bot.current_msg_index]
        random_emoji = random.choice(EMOJIS)
        
        # التنسيق النهائي للرسالة
        final_msg = f"<@{WASEET_ID}> {base_msg} {random_emoji}"
        
        try:
            await channel.send(final_msg)
            print(f"✅ أرسلت الرسالة رقم {bot.current_msg_index + 1} وسويت منشن للوسيط.")
            
            # نجهز للرسالة اللي بعدها في القائمة
            bot.current_msg_index = (bot.current_msg_index + 1) % len(MESSAGES)
            
        except Exception as e:
            print(f"❌ خطأ في الإرسال: {e}")
    else:
        print(f"⚠️ مو قادر أشوف القناة {CHANNEL_ID}")

@bot.event
async def on_ready():
    print("-" * 30)
    print(f'✅ البوت {bot.user} شغال!')
    print(f'✅ راح يرسل منشن لـ {WASEET_ID} كل 5 دقايق.')
    print("-" * 30)
    if not auto_vouch.is_running():
        auto_vouch.start()

bot.run("MTQ3MzEwNTA2MDk3MDg4OTI3OQ.Gnxprv.nP5_XEYVu0z7_XBt9o3iKytkkIHXfLE-3ECJh0")