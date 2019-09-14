def to_dict(data):
  """
  "question=marriged&answer={}&next_question={}".format(self.data_text, self.next_question)
  形式のevent.dataをDict形式に変換して返す
  """

  return_dict = {}
  # &で要素を分割
  splited_data = data.split("&")
  for item in splited_data:
    # 分割された各要素を=で分割
    key = item.split("=")[0]
    value = item.split("=")[1]

    return_dict[key] = value
  
  return return_dict