import boto3
import json
from datetime import datetime, timedelta

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('dev-ddb-sessions')


def store_session(user_id):
  
  # 対象のuser_idのセッションレコードがあるかを確認
  session = query(user_id)
  print("Session : {}".format(session))
  if session is None:
    # Sessionが存在しない場合、新規に作成
    print("session created for user {}".format(user_id))
    put(user_id, "next_question", 1)
    update(user_id, "updated", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
  else:
    updated = session.get("updated")
    print("session updated date : {}".format(updated))
    session_updated = datetime.strptime(updated, '%Y-%m-%d %H:%M:%S') if updated is not None else datetime.now() - timedelta(30)
    # 前回のSession更新から１日経っている場合、Sessionを破棄して新たに作成
    if datetime.now() - timedelta(1) > session_updated:
      print("session created for user {}".format(user_id))
      update(user_id, "next_question", 1)
      update(user_id, "updated", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 前回のSession更新から１日以内である場合、next_questionを更新(increment)
    else:
      print("session updated for user {}".format(user_id))
      update(user_id, "next_question", session.get("next_question") + 1)
      update(user_id, "updated", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def clear_session(user_id):
  # 対象のSessionをクリアする関数
  session = query(user_id)
  if session is None:
    print("session is not found")
    pass
  else:
    print("session cleared for {}".format(user_id))
    delete(user_id)


def put(id, key, value):
  """
  DynamoDBにレコードを登録する関数
  @Param user_id ハッシュキー
  """
  result = table.put_item(
    Item = {
      "user_id" : id,
      key : value,
    }
  )
  print(result)
  return result

def update(id, key, value):
  """
  DynamoDBのレコードを更新する関数
  @Param user_id ハッシュキー
  """
  result = table.update_item(
    Key = {
      'user_id' : id,
    },
    UpdateExpression="set {} = :i".format(key),
    ExpressionAttributeValues={
      ':i': value
    },
    ReturnValues="UPDATED_NEW"
  )
  print(result)
  return result

def delete(id):
  """
  DynamoDBのレコードを削除する関数
  @Param user_id ハッシュキー
  """
  result = table.delete_item(
    Key = {
      "user_id" : id
    }
  )
  print(result)
  return result

def query(id):
  """
  DynamoDBから検索する関数
  @Param user_id ハッシュキー
  @return 検索結果
  """
  result = table.get_item(
    Key = {
      'user_id' : id,
    }
  )
  print(result.get("Item"))
  return result.get("Item")