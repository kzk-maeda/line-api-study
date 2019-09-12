import json

class QuestionClass():
  def __init__(self, question_text, contents_list):
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

  def create_question(self):
    return self.base_bubble
