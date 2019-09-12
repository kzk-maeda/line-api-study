import json
import contents.questions as q

from flask import Flask, request, abort

from linebot import (
  LineBotApi, WebhookHandler
)

from linebot.exceptions import (
  InvalidSignatureError
)

from linebot.models import (
  MessageEvent, PostbackEvent, TextMessage, TextSendMessage, FlexSendMessage
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
  # app.logger.info("Health Check : OK" )
  print("Health Check : OK" )
  return "OK"


@app.route("/callback", methods=['POST'])
def callback():
  # get X-Line-Signature header value
  signature = request.headers['X-Line-Signature']

  # get request body as text
  body = request.get_data(as_text=True)
  # app.logger.info("Request_body : " + body)
  print("Request_body : " + body)

  # handle webhook body
  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)
  
  return 'OK'

# 初回メッセージを受け取ったときに実行
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  
  question_text = "あなたの性別を教えてください"
  contents_list = [
    {
      "type": "button",
      "style": "primary",
      "action": {
        "type": "postback",
        "label": "Man",
        "data": "action=store&storeId=000000",
        "displayText":"Man"
      }
    },
    {
      "type": "button",
      "style": "primary",
      "action": {
        "type": "postback",
        "label": "Woman",
        "data": "action=store&storeId=000000",
        "displayText":"Woman"
      }
    }
  ]
  contents = q.QuestionClass(question_text, contents_list)
  
  message = FlexSendMessage(alt_text="hello", contents=contents.create_question())

  line_bot_api.reply_message(
    event.reply_token,
    message
  )

# Postbackを受け取った時に実行
@handler.add(PostbackEvent)
def handle_postback(event):

  print(event)
  if event.postback.data == "action=store&storeId=000000":
    question_text = "あなたの年齢を教えてください"
    contents_list = [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "postback",
          "label": "20代",
          "data": "action=store&age=20",
          "displayText":"20代"
        }
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "postback",
          "label": "30代",
          "data": "action=store&age=30",
          "displayText":"30代"
        }
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "postback",
          "label": "40代",
          "data": "action=store&age=40",
          "displayText":"40代"
        }
      }
    ]
    contents = q.QuestionClass(question_text, contents_list)
    message = FlexSendMessage(alt_text="hello", contents=contents.create_question())

    line_bot_api.reply_message(
      event.reply_token,
      message
    )
  else:
    message = "Done"
    line_bot_api.reply_message(
      event.reply_token,
      message
    )

if __name__ == "__main__":
    app.run()