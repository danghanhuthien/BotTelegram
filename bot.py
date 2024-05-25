from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Hàm bắt đầu bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Google", callback_data='https://www.google.com')],
        [InlineKeyboardButton("YouTube", callback_data='https://www.youtube.com')],
        [InlineKeyboardButton("GitHub", callback_data='https://www.github.com')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Chọn một liên kết:', reply_markup=reply_markup)

# Hàm xử lý callback
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Bạn đã chọn: {query.data}")

def main() -> None:
    token = os.getenv("7134062086:AAGQMuhLWR4jL7ieFTa9Uwywrmi3lc5_upM")
    application = Application.builder().token(token).build()

    # Đăng ký hàm start với lệnh /start
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Bắt đầu bot
    application.run_polling()

if __name__ == '__main__':
    main()
