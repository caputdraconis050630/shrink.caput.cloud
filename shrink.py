import boto3
import os
import random
import string
import botocore
from botocore.client import Config

DEBUG = True

# 랜덤 키값 생성
def generate_random(n):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(n))

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
    # DynamoDB 서비스 리소스를 생성합니다.
    dynamodb = boto3.resource('dynamodb')

    # 사용할 DynamoDB 테이블 이름
    table_name = os.environ['TABLE_NAME']

    # DynamoDB 테이블 객체를 가져옵니다.
    table = dynamodb.Table(table_name)
    
    native_url = event['value']
    cdn_prefix = os.environ['HOST']
    
    if not 'shrink.caput.cloud/key' in native_url:
        exists, response = exists_dynamoDB(table, 'orig', native_url)
    
        if exists: # 이미 있음
            print(response)
            short_key = response[0]['short_key']
        else: # 없음
            while (True):
                short_key = generate_random(7)
                # short key 가 이미 있는 키인가?
                print(short_key)
                exists, response = exists_dynamoDB(table, 'short_key', short_key)
                if not exists:
                    break
                else:
                    print("We got a short_key collision: " + short_key + ". Retrying.")
            
    
        print("We got a valid short_key: " + short_key)

        ### 새로운 원본 URL + 키값 저장
        response = table.put_item(
           Item={
               "short_key": short_key,
               "orig": native_url
           }
        )

        public_short_url = "https://" + cdn_prefix + "/key/" + short_key;
    else:
        public_short_url: native_url

    return {
        'body': { 
            "url_short": public_short_url, 
            "url_long": native_url 
        }
    }
        