from telegram.ext import Application, CommandHandler

TOKEN = "ใส่_BOT_TOKEN_ใหม่_ของคุณ"

async def start(update, context):
    await update.message.reply_text(
        "Bot Online 🚀"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.run_polling()
