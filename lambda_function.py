import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def lambda_handler(event, context):
    try:
        http_method = event['httpMethod']

        # POST: to create a new record
        if http_method == 'POST':
            student = json.loads(event['body'])
            table.put_item(Item=student)
            return {
                'statusCode': 200,
                'body': json.dumps('Student record added successfully')
            }

        # GET: to fetch an existing record by student_id
        elif http_method == 'GET':
            student_id = event['queryStringParameters']['student_id']
            response = table.get_item(Key={'student_id': student_id})
        
            if 'Item' in response:
                item = response['Item']
                ordered_item = {
                    'student_id': item['student_id'],
                    'name': item['name'],
                    'university': item['university'],
                    'course': item['course']
                }
                return {
                    'statusCode': 200,
                    'body': json.dumps(ordered_item)
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'error': 'Student record not found'})
                }


        # PUT: to update an existing record 
        elif http_method == 'PUT':
            student_id = event['queryStringParameters']['student_id']
            student = json.loads(event['body'])
            table.update_item(
                Key={'student_id': student_id},
                UpdateExpression='SET #name = :name, #university = :university, #course = :course',
                ExpressionAttributeNames={
                    '#name': 'name',
                    '#university': 'university',
                    '#course': 'course'
                },
                ExpressionAttributeValues={
                    ':name': student['name'],
                    ':university': student['university'],
                    ':course': student['course']
                }
            )
            return {
                'statusCode': 200,
                'body': json.dumps('Student record updated successfully')
            }

        # DELETE: to remove an existing record
        elif http_method == 'DELETE':
            student_id = event['queryStringParameters']['student_id']
            table.delete_item(Key={'student_id': student_id})
            return {
                'statusCode': 200,
                'body': json.dumps('Student record deleted successfully')
            }

        # Unsupported HTTP method
        else:
            return {
                'statusCode': 405,
                'body': json.dumps({'error': f'Method {http_method} not allowed'})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
