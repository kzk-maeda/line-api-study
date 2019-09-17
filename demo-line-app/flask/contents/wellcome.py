class WellcomeClass():
  def __init__(self):
    pass

  def create_wellcome_board(self):
    self.contents = {
      "type": "bubble",
        "header": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "全20問の質問に答えてあなたの妊娠力を診断しましょう",
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
                  #   "type": "postback",
                  #   "label": "診断スタート！",
                  #   "data": "diagnosis=start&next_question=1",
                  #   "displayText":"スタート！"
                  # }
                    "type": "uri",
                    "label": "診断スタート！",
                    "uri": "line://app/1619401802-dAP02MZ4"
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
            "separator": False
          }
        }
      }
    return self.contents    