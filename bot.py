from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

TOKEN = "8262051249:AAEz_51RhbyjfGpbIA1CedUB3iSN7U-EEP4"
ADMIN_CHAT_ID = 1115210742

NOME, TELEFONO, SERVIZIO = range(3)

servizi_keyboard = [
    ["Impianto elettrico", "Fotovoltaico"],
    ["Preventivo", "Guasto / Assistenza"]
]

reply_markup = ReplyKeyboardMarkup(servizi_keyboard, one_time_keyboard=True, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Benvenuto!\n\n"
        "Per offrirti il miglior servizio, iniziamo con qualche informazione.\n\n"
        "👉 Come ti chiami?"
    )
    return NOME

async def nome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["nome"] = update.message.text
    await update.message.reply_text("Perfetto 👍\n\n📞 Inserisci il tuo numero di telefono:")
    return TELEFONO

async def telefono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["telefono"] = update.message.text
    await update.message.reply_text("Ottimo 👌\n\n⚡ Seleziona il servizio:", reply_markup=reply_markup)
    return SERVIZIO

async def servizio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = context.user_data["nome"]
    telefono = context.user_data["telefono"]
    servizio = update.message.text

    messaggio = (
        f"📩 NUOVA RICHIESTA\n\n"
        f"👤 Nome: {nome}\n"
        f"📞 Telefono: {telefono}\n"
        f"🔧 Servizio: {servizio}"
    )

    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=messaggio)

    await update.message.reply_text(
        "✅ Richiesta ricevuta!\n\n"
        "Un nostro operatore ti contatterà al più presto.\n"
        "Grazie per averci scelto 🙌"
    )

    return ConversationHandler.END

app = ApplicationBuilder().token(TOKEN).build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        NOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, nome)],
        TELEFONO: [MessageHandler(filters.TEXT & ~filters.COMMAND, telefono)],
        SERVIZIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, servizio)],
    },
    fallbacks=[],
)

app.add_handler(conv_handler)

app.run_polling()
