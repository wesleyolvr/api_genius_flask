import boto3



class ConexaoBD:
    def __init__(self,table_name):
        self.dynamodb = boto3.resource(
            'dynamodb', region_name='us-east-1')
        self.table = self.dynamodb.Table(table_name)

    
    def put_item(self, id, artist, hits):
        response = self.table.put_item(
            item={
                'id': id,
                'artist': artist,
                'hits': hits
            }
        )
        return response['Item']
    
    def get_item(self, id):
        response = self.table.get_item(
            Key={
                'id': id
            }
        )
        return response['Item']
    
    def update_item(self, id, artist, hits):
        response = self.table.update_item(
            Key={
                'id': id
            },
            UpdateExpression="set artist = :a, hits = :h",
            ExpressionAttributeValues={
                ':a': artist,
                ':h': hits
            },
            ReturnValues="UPDATED_NEW"
        )
        return response['Attributes']


    def delete_item(self, id):
        response = self.table.delete_item(
            Key={
                'id': id
            }
        )
        return response['Attributes']