import json
import base64
import boto3
import copy

from datetime import datetime

def lambda_handler(event, context):

    client = boto3.client('dynamodb')  #initiate client for DynamoDB

    for record in event['Records']:  #go over records
#        print("record ", record)
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])

        # decode the bytes into a string
        str_record = str(payload,'utf-8')
        print('str_record ', str_record)
        
        #transform the json string into a dictionary
        track_record = json.loads(str_record)

        # create Customer Row in SpotifyTrack table
        track_key = dict()
        print('track_record ', track_record)
        track_key.update({'trackID': {"S": str(track_record['trackID'])}}) #track ID will be a primary key
        print("track_key ", track_key)

        track_dict = copy.deepcopy(track_record)  #duplicate dictionary 
        track_dict.pop('trackID',None)
        track_json = json.dumps(track_dict)

        track_attribute =dict()
        track_attribute.update({str(track_record['country']): {'Value':{"S":track_json},"Action":"PUT"}})
        print("track_attribute ", track_attribute)
        
        # Update item in the table. Primarry key is trackID; info about track is stored in attributes. Attribute names are countries.
        response = client.update_item(TableName='SpotifyTracks', Key = track_key, AttributeUpdates = track_attribute)
        print("response", response)

    return 'Successfully processed {} records.'.format(len(event['Records']))
