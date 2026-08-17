from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator

TOKEN = "8897067455:AAEekf-xYmjCE-D7HGfv2sh5KMdxyKTYSAM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اهلا! 👋\nابعتلي اي كلمة او جملة وانا اترجمهالك للانجليزي فورا 🇪🇬➡️🇺🇸")

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    try:
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        await update.message.reply_text(f"الترجمة:\n{translated}")
    except:
        await update.message.reply_text("في مشكلة في الترجمة، جرب تاني")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

print("البوت شغال...")
app.run_polling()
