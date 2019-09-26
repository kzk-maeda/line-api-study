import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ddb-diagnosis')

def put(id, key, value):
  """
  DynamoDBにレコードを登録する関数
  @Param id ハッシュキー
  @Param name レンジキー
  """
  table.put_item(
    Item = {
      "id" : id,
      key : value,
    }
  )


def update(id, key, value):
  """
  DynamoDBのレコードを更新する関数
  @Param id ハッシュキー
  """
  table.update_item(
    Key = {
      'id' : id,
    },
    UpdateExpression="set {} = :i".format(key),
    ExpressionAttributeValues={
      ':i': value
    },
    ReturnValues="UPDATED_NEW"
  )


def query(id):
  """
  DynamoDBから検索する関数
  @Param id ハッシュキー
  @Param name レンジキー
  @return 検索結果
  """
  result = table.get_item(
    Key = {
      'id' : id,
    }
  )
  return result


def scan():
  """
  DynamoDBから全件検索する関数
  @return 検索結果
  """
  result = table.scan()
  return result

