from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('1l6c8hOlVNiLh23YRFrdl1TxJxK4KUZppI9dRaDscY5fX50D6xEBhb4D0ZglujEA1+MiFoFV2N5pl1KIYZmlq8/WSmxf2b4WVhcvfjJoUH7ISxjUDK55FzS1B3DhC6X4/m4ZM0/0bN7HRNzLzKToewdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3692fbc3db90c226b12e3f91130e2f9f')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
