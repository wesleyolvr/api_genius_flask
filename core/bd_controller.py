import boto3
import requests
from botocore.exceptions import ClientError

dynamo_client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
TableName='genius'


def get_item(name):
    table = dynamodb.Table(TableName)
    try:
        response = table.get_item(
            Key=
            {
                'artist': name,
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response
    
def get_all_items():
    table = dynamodb.Table(TableName)
    return table.scan()

def load_items(items):
    table = dynamodb.Table(TableName)
    artist = items['artist']
    print(f'carregando artista {artist}')
    return table.put_item(
        Item=items
        )

def delete(name):
    table = dynamodb.Table(TableName)
    return table.delete_item(
        Key={
            'artist': name,
        }
    )
