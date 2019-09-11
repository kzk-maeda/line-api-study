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
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "image",
          "url": "https://line-objects-dev.com/flex/bg/eiji-k-1360395-unsplash.jpg",
          "position": "relative",
          "size": "full",
          "aspectMode": "cover",
          "aspectRatio": "1:1",
          "gravity": "center"
        },
        {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "Brown Hotel",
                  "weight": "bold",
                  "size": "xl",
                  "color": "#ffffff"
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "margin": "md",
                  "contents": [
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                    },
                    {
                      "type": "text",
                      "text": "4.0",
                      "size": "sm",
                      "color": "#d6d6d6",
                      "margin": "md",
                      "flex": 0
                    }
                  ]
                }
              ]
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "¥62,000",
                  "color": "#a9a9a9",
                  "decoration": "line-through",
                  "align": "end"
                },
                {
                  "type": "text",
                  "text": "¥42,000",
                  "color": "#ebebeb",
                  "size": "xl",
                  "align": "end"
                }
              ]
            }
          ],
          "position": "absolute",
          "offsetBottom": "0px",
          "offsetStart": "0px",
          "offsetEnd": "0px",
          "backgroundColor": "#00000099",
          "paddingAll": "20px"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "SALE",
              "color": "#ffffff"
            }
          ],
          "position": "absolute",
          "backgroundColor": "#ff2600",
          "cornerRadius": "20px",
          "paddingAll": "5px",
          "offsetTop": "10px",
          "offsetEnd": "10px",
          "paddingStart": "10px",
          "paddingEnd": "10px"
        }
      ],
      "paddingAll": "0px"
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