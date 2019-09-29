import json
from datetime import datetime
import contents.questions as q
import contents.wellcome as wb
import contents.result as rs
import library.mod_event_data as mod
import library.operate_dynamodb as ddb

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

  wellcome = wb.WellcomeClass()
  contents = wellcome.create_wellcome_board()
  
  message = FlexSendMessage(alt_text="hello", contents=contents)

  line_bot_api.reply_message(
    event.reply_token,
    message
  )

def send_line_api(event, contents, alt_text="hello"):
  message = FlexSendMessage(alt_text=alt_text, contents=contents)

  line_bot_api.reply_message(
    event.reply_token,
    message
  )

# Postbackを受け取った時に実行
@handler.add(PostbackEvent)
def handle_postback(event):
  question = q.QuestionClass()

  # print(event)
  # event.postback.data をdict形式に分割
  data = mod.to_dict(event.postback.data)
  user_id = event.source.user_id
  question_param = data.get('question')
  answer_param = data.get('answer')
  print('{} / {} / {}'.format(user_id, question_param, answer_param))
  if answer_param is not None:
    answer_data = {}
    answer_data['answer'] = answer_param
    answer_data['score'] = 0
    answer_data['updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ddb.register_answer(user_id, question_param, answer_data)

  next = data.get('next_question')
  # 1 : 結婚しているかどうか
  if next == "1":
    contents = question.create_question_marriged()
    send_line_api(event, contents)
  # 2-1 : (第１問がNoのとき)妊活期間
  elif next == "2-1":
    contents = question.create_question_pregenancy_period()
    send_line_api(event, contents)
  # 2-2 : 医師に相談したかどうか
  elif next == "2-2":
    contents = question.create_question_whether_consulted_to_doctor()
    send_line_api(event, contents)
  # 2-3 : 配偶者の精液検査
  elif next == "2-3":
    contents = question.create_question_whether_semen_exam()
    send_line_api(event, contents)
  # 2-4 : 配偶者の精液検査結果
  elif next == "2-4":
    contents = question.create_question_semen_exam_result()
    send_line_api(event, contents)
  # 3-1 : (2-3か1から)年齢
  elif next == "3-1":
    contents = question.create_question_age()
    send_line_api(event, contents)
  # 3-2 : 身長
  elif next == "3-2":
    contents = question.create_question_height()
    send_line_api(event, contents)
  # 3-3 : 体重
  elif next == "3-3":
    contents = question.create_question_weight()
    send_line_api(event, contents)
  # 4 : 妊娠経験
  elif next == "4":
    contents = question.create_question_whether_pregenancy()
    send_line_api(event, contents)
  # 5 : (4がYesのとき)出産経験
  elif next == "5":
    contents = question.create_question_whether_birth()
    send_line_api(event, contents)
  # 6-1 : (4か5から)生理周期
  elif next == "6-1":
    contents = question.create_question_menstrual_cycle()
    send_line_api(event, contents)
  # 6-2 : 生理痛
  elif next == "6-2":
    contents = question.create_question_menstrual_pain()
    send_line_api(event, contents)
  # 6-3 : 喫煙
  elif next == "6-3":
    contents = question.create_question_smoke()
    send_line_api(event, contents)
  # 6-4 : 飲酒
  elif next == "6-4":
    contents = question.create_question_drink()
    send_line_api(event, contents)
  # 6-5 : AMH検査
  elif next == "6-5":
    contents = question.create_question_amh()
    send_line_api(event, contents)
  # 6-6 : AMH検査結果
  elif next == "6-6":
    contents = question.create_question_amh_result()
    send_line_api(event, contents)
  # 6-7 : 症例
  elif next == "6-7":
    contents = question.create_question_disease_cases()
    send_line_api(event, contents)
  # 7-1 : 知人への相談
  elif next == "7-1":
    contents = question.create_question_whether_consulted_to_acquaintance()
    send_line_api(event, contents)
  # 7-2 : 利用規約
  elif next == "7-2":
    contents = question.create_question_terms_of_service()
    send_line_api(event, contents)
  elif next == "result":
    result = rs.culc_result(user_id)
    # send_line_api(event, result)

# LIFFからPOSTを受け取った時に実行
@app.route("/liff")
def post_from_liff():
  # app.logger.info("Health Check : OK" )
  print("Health Check : OK" )
  return "OK"

if __name__ == "__main__":
    app.run()