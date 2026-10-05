from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8610480188:AAFT3qY2yo9CDrveJYBIHFRl4D5uyo6LpYE"

def ai_phishing_check(url: str) -> bool:
    url = url.lower()
    bad_words = ["free", "gift", "win", "login", "verify", "bank", "update", "secure"]
    score = sum(1 for w in bad_words if w in url)
    if score >= 2 or "@" in url or url.count("-") > 3:
        return True
    return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working! Send link")

async def check_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    is_scam = ai_phishing_check(url)
    if is_scam:
        await update.message.reply_text("🚨 Danger! Scam link")
    else:
        await update.message.reply_text("✅ Safe link")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_link))
print("Bot is running...")
app.run_polling()