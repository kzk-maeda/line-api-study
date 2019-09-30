import json

class QuestionClass():
  def __init__(self):
    pass
  
  # 共通デザイン
  def create_base(self, question_text, contents_list):
    self.base_bubble = {
      "type": "bubble",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": question_text,
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
              "contents": contents_list,
              "flex": 1
            }
          ],
          "spacing": "md",
          "paddingAll": "12px"
        },
        "styles": {
          "footer": {
            "separator": False
          }
        }
      }
    return self.base_bubble
  
  # 共通コンポーネント
  def generate_button_contents_list(self, question_label, contents_items):
    self.question_label = question_label
    self.contents_list = []
    for i in contents_items:
      self.label_text = i.get("label_text")
      self.data_text = i.get("data_text")
      self.next_question = i.get("next_question")

      self.component = {
        "type": "button",
          "style": "primary",
          "action": {
            "type": "postback",
            "label": self.label_text,
            "data": "question={}&answer={}&next_question={}".format(self.question_label, self.data_text, self.next_question),
            "displayText": self.label_text
          }
        }
      self.contents_list.append(self.component)
    return self.contents_list
  
  def generate_text_contents(self):
    self.text_contents = "半角数字で入力してください"
    self.contents_list = []

    self.component = {
      "type": "text",
      "text": self.text_contents
    }
    self.contents_list.append(self.component)
    
    return self.contents_list

  # 1 : 結婚しているかどうか
  def create_question_marriged(self):
    self.question_text = "現在結婚していますか？"
    self.question_label = "marriged"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "2-1"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "3-1"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents

  # 2-1 : (第１問がYesのとき)妊活期間
  def create_question_pregenancy_period(self):
    self.question_text = "どのくらいの期間妊活をしていますか？"
    self.question_label = "pregenancy_period"
    self.contents_items = [
      {
        "label_text": "1年",
        "data_text": "1",
        "next_question": "2-2"
      },
      {
        "label_text": "2年",
        "data_text": "2",
        "next_question": "2-2"
      },
      {
        "label_text": "3-4年",
        "data_text": "3-4",
        "next_question": "2-2"
      },
      {
        "label_text": "5-6年",
        "data_text": "5-6",
        "next_question": "2-2"
      },
      {
        "label_text": "7-8年",
        "data_text": "7-8",
        "next_question": "2-2"
      }
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents

  
  # 2-2 : 医師に相談したかどうか
  def create_question_whether_consulted_to_doctor(self):
    self.question_text = "妊活を始めてから医師には相談しましたか？"
    self.question_label = "whether_consulted_to_doctor"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "2-3"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "2-3"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents

  # 2-3 : 配偶者の精液検査
  def create_question_whether_semen_exam(self):
    self.question_text = "配偶者は精液検査を受けましたか？"
    self.question_label = "whether_semen_exam"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "2-4"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "3-1"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
  
  # 2-4 : 精液検査の結果
  def create_question_semen_exam_result(self):
    self.question_text = "配偶者の精液検査の結果は？"
    self.question_label = "semen_exam_result"
    self.contents_items = [
      {
        "label_text": "60%以上",
        "data_text": "60%以上",
        "next_question": "3-1"
      },
      {
        "label_text": "40-59%",
        "data_text": "40-59%",
        "next_question": "3-1"
      },
      {
        "label_text": "20-39%",
        "data_text": "20-39%",
        "next_question": "3-1"
      },
      {
        "label_text": "0-19%",
        "data_text": "0-19%",
        "next_question": "3-1"
      },
      {
        "label_text": "不明",
        "data_text": "不明",
        "next_question": "3-1"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
  
  # 3-1 : (2-3か1から)年齢
  def create_question_age(self):
    self.question_text = "現在何歳ですか？"
    self.question_label = "age"
    self.contents_list = self.generate_text_contents()
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
  
  # 3-2 : 身長
  def create_question_height(self):
    self.question_text = "身長は何cmですか？"
    self.question_label = "height"
    self.contents_list = self.generate_text_contents()
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents

  # 3-3 : 体重
  def create_question_weight(self):
    self.question_text = "体重は何キロですか？"
    self.question_label = "weight"
    self.contents_list = self.generate_text_contents()
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
  
  # 4 : 妊娠経験
  def create_question_whether_pregenancy(self):
    self.question_text = "以前妊娠したことはありますか？"
    self.question_label = "whether_pregenancy"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "5"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "6-1"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
  
  # 5 : (4がYesのとき)出産経験
  def create_question_whether_birth(self):
    self.question_text = "出産経験はありますか？"
    self.question_label = "whether_birth"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "6-1"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "6-1"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents

  # 6-1 : (4か5から)生理周期
  def create_question_menstrual_cycle(self):
    self.question_text = "生理周期は順調ですか？"
    self.question_label = "menstrual_cycle"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "6-2"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "6-2"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents

  # 6-2 : 生理痛
  def create_question_menstrual_pain(self):
    self.question_text = "生理痛は重いですか？"
    self.question_label = "menstrual_pain"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "6-3"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "6-3"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents

  # 6-3 : 喫煙
  def create_question_smoke(self):
    self.question_text = "喫煙しますか？"
    self.question_label = "smoke"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "6-4"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "6-4"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
    
  # 6-4 : 飲酒
  def create_question_drink(self):
    self.question_text = "1日平均どのくらいお酒を飲みますか？"
    self.question_label = "drink"
    self.contents_items = [
      {
        "label_text": "飲まない",
        "data_text": "0",
        "next_question": "6-5"
      },
      {
        "label_text": "時々飲む",
        "data_text": "1",
        "next_question": "6-5"
      },
      {
        "label_text": "よく飲む",
        "data_text": "2",
        "next_question": "6-5"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
    
  # 6-5 : AMH検査
  def create_question_amh(self):
    self.question_text = "AMH（卵巣年齢）血液検査を1年以内に受けましたか？"
    self.question_label = "amh"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "6-6"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "6-7"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
  
  # 6-6 : AMHの数値入力
  def create_question_amh_result(self):
    self.question_text = "AMH検査の数値を入力してください"
    self.question_label = "amh_result"
    self.contents_items = [
      {
        "label_text": "dummy",
        "data_text": "dummy",
        "next_question": "6-7"
      }
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents

  # 6-7 : 症例
  def create_question_disease_cases(self):
    self.question_text = "以下に該当する症状はありますか？"
    self.question_label = "disease_cases"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "7-1"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "7-1"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
    
  # 7-1 : 知人への相談
  def create_question_whether_consulted_to_acquaintance(self):
    self.question_text = "友達や家族に妊活や妊娠のための健康について話したことはありますか？"
    self.question_label = "whether_consulted_to_acquaintance"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "7-2"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "7-2"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
    
  # 7-2 : 利用規約
  def create_question_terms_of_service(self):
    self.question_text = "利用規約に同意しますか？"
    self.question_label = "terms_of_service"
    self.contents_items = [
      {
        "label_text": "はい",
        "data_text": "yes",
        "next_question": "result"
      },
      {
        "label_text": "いいえ",
        "data_text": "no",
        "next_question": "result"
      },
    ]
    self.contents_list = self.generate_button_contents_list(self.question_label, self.contents_items)
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
    
