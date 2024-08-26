import os
import boto3
from botocore.client import Config


def exists_dynamoDB(table, field_name, field_value):
    # 스캔 조건 설정
    scan_kwargs = {
        'FilterExpression': f"{field_name} = :value",
        'ExpressionAttributeValues': {
            ':value': field_value
        }
    }

    # 스캔 실행
    response = table.scan(**scan_kwargs)
    
    # 결과 반환
    items = response.get('Items', [])
    if items:
        return True, items
    else:
        return False, []


def lambda_handler(event, context):
    short_key = event.get("key")
            
    # DynamoDB 서비스 리소스를 생성합니다.
    dynamodb = boto3.resource('dynamodb')

    # 사용할 DynamoDB 테이블 이름
    table_name = os.environ['TABLE_NAME']

    # DynamoDB 테이블 객체를 가져옵니다.
    table = dynamodb.Table(table_name)
    
    exists, resp = exists_dynamoDB(table, 'short_key', short_key)
            
    if exists:
        # 존재
        original_url = resp[0]['orig']
        if not '://' in original_url:
            original_url = 'http://' + original_url
        print(original_url)
        return {
            'statusCode': 301,
            'headers': {
                'Location': original_url
            },
            'body': ''
        }
    else:
        # 존재 X
        return {
            'statusCode': 404,
            'body': "Not Found Key"
        }