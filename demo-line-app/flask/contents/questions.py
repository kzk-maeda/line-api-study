import json

class QuestionClass():
  def __init__(self):
    pass
    
  def create_base(self, question_text, contents_list):
    self.base_bubble = {
      "type": "bubble",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": self.question_text,
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
              "contents": self.contents_list,
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

  def create_question_marriged(self):
    self.question_text = "現在妊娠していますか？"
    self.contents_list = [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "postback",
          "label": "はい",
          "data": "question=marriged&answer=yes",
          "displayText":"はい"
        }
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "postback",
          "label": "いいえ",
          "data": "question=marriged&answer=yes",
          "displayText":"いいえ"
        }
      }
    ]
    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents

  def create_question_pregenancy_period(self):
    self.question_text = "どのくらいの期間妊活をしていますか？"
    self.contents_list = []

    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
  
  def create_question_whether_consulted(self):
    self.question_text = "妊活を始めてから医師には相談しましたか？"
    self.contents_list = []

    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents

  def create_question_whether_semen_exam(self):
    self.question_text = "配偶者は精液検査を受けましたか？"
    self.contents_list = []

    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
  
  def create_question_age(self):
    self.question_text = "現在何歳ですか？"
    self.contents_list = []

    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents

  def create_question_weight(self):
    self.question_text = "体重は何キロですか？"
    self.contents_list = []

    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents
  
  def create_question_whether_pregenancy(self):
    self.question_text = "以前妊娠したことはありますか？"
    self.contents_list = []

    self.contents = self.create_base(self.question_text, self.contents_list)
    return self.contents