import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('dev-ddb-diagnosis')

def register_answer(id, key, value):
  # idのレコードがすでに存在するか確認
  if query(id) is None:
    # idレコードが存在しない場合、新規レコードとして登録
    put(id, key, value)
  else:
    # idレコードが存在する場合、既存レコードを更新
    update(id, key, value)


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
  print(result)
  return result


def scan():
  """
  DynamoDBから全件検索する関数
  @return 検索結果
  """
  result = table.scan()
  print(result)
  return result

