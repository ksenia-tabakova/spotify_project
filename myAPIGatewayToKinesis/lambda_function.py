import json
import boto3

def lambda_handler(event, context):

    print("MyEvent: ", event)

    try:
        method = event['requestContext']['httpMethod']
    except KeyError:
        method = event['context']['http-method']

    if method == "POST":

        incoming_record = event['body']  # data comes in body
        recordstring = json.dumps(incoming_record) #  convert record to json string

        client = boto3.client('kinesis')  #initiate clinet for Kinesis
        response = client.put_record(  #put single record to the Kinesis datastream
            StreamName='mySpotifyKinesis',
            Data= incoming_record,
            PartitionKey='string'
        )
        return {
            'statusCode': 200,
            'body': json.dumps(p_record)
        }
    else:
        return {
            'statusCode': 501,
            'body': json.dumps("Server Error")
        }
