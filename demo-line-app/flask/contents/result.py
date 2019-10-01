import json
import sys
sys.path.append('../')

import library.operate_dynamodb as ddb


def culc_result(user_id):
  print("culcurate answer start")
  ans = ddb.get_answer(user_id)
  print(ans)

  return ans