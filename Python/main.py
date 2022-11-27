from telegram.ext import *
from datetime import date

API_KEY = "5949204184:AAE26em2OpaRD_44tUfsNZCHFooBZCJbWok"
admin_id = "602622095"


def start(update, context):
    user_id = str(update.message.from_user.id)

    if user_id == admin_id:
        day_count_text = "<code>YOu know what this bot does, Fifa. XOXO</code>"

        context.bot.send_message(text=day_count_text, chat_id=user_id, parse_mode="HTML")


def stats(update, context):
    user_id = str(update.message.from_user.id)

    if user_id == admin_id:
        d0 = date(2022, 11, 23)
        d1 = date.today()
        difference = d1 - d0

        day_count_text = f"<code>It's been {difference.days} days!</code>"

        context.bot.send_message(text=day_count_text, chat_id=user_id, parse_mode="HTML")


def error(update, context):
    print(f"Update {update} caused error.\n {context.error}")


def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stats", stats))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    print("Bot started...")

    main()






