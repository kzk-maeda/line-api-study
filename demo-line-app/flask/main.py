import json

from flask import Flask, request, abort

from linebot import (
  LineBotApi, WebhookHandler
)

from linebot.exceptions import (
  InvalidSignatureError
)

from linebot.models import (
  MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)

app = Flask(__name__)


# Read Keys
with open('env.json', 'r') as f:
  data = json.load(f)
  ACCESS_TOKEN = data.get('access_token')
  SECRET = data.get('secret')

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/health")
def health_check():
  app.logger.info("Health Check : OK" )
  print("Health Check : OK" )
  return "OK"


@app.route("/callback", methods=['POST'])
def callback():
  # get X-Line-Signature header value
  signature = request.headers['X-Line-Signature']

  # get request body as text
  body = request.get_data(as_text=True)
  app.logger.info("Request_body : " + body)
  print("Request_body : " + body)

  # handle webhook body
  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)
  
  return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  # line_bot_api.reply_message(
  #   event.reply_token,
  #   TextSendMessage(text=event.message.text)
  # )
  contents_string = """
  {
    "type": "bubble",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "あなたの性別を教えてください",
          "color": "#ffffff",
          "align": "start",
          "size": "md",
          "gravity": "center"
        }
      ],
      "backgroundColor": "#27ACB2",
      "paddingTop": "19px",
      "paddingAll": "12px",
      "paddingBottom": "16px"
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "spacing": "md",
          "contents": [
            {
              "type": "button",
              "style": "primary",
              "action": {
                "type": "uri",
                "label": "Man",
                "uri": "https://example.com"
              }
            },
            {
              "type": "button",
              "style": "primary",
              "action": {
                "type": "uri",
                "label": "Woman",
                "uri": "https://example.com"
              }
            }
          ],
          "flex": 1
        }
      ],
      "spacing": "md",
      "paddingAll": "12px"
    },
    "styles": {
      "footer": {
        "separator": false
      }
    }
  }
  """
  message = FlexSendMessage(alt_text="hello", contents=json.loads(contents_string))

  line_bot_api.reply_message(
    event.reply_token,
    # TextSendMessage(text="自動応答メッセージ")
    message
  )

if __name__ == "__main__":
    app.run()