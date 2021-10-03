from __future__ import print_function

import base64
import json
import boto3
from datetime import datetime

#make s3 client
s3_client = boto3.client("s3")

def lambda_handler(event, context):

    kinesisRecords = []  #initialize empty list where records will be added
    for record in event['Records']:  
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        print("Decoded payload: " + payload)
        # Get eventID that will be used to make unique file names
        eventID = record['kinesis']['sequenceNumber']
        print('eventID ', eventID)
        kinesisRecords.append(payload)
        
    #make a string out of list
    bacth_string = '\n'.join(kinesisRecords)
    string_json = json.dumps(bacth_string)
    print("string_json ", string_json)
    
    #generate name for the file with the eventID
    mykey = 'output-' + eventID + '.json'
    
    #put the file into S3 bucket
    response = s3_client.put_object(Body=bacth_string, Bucket="myspotifybucket", Key = mykey)
    return 'Successfully processed {} records.'.format(len(event['Records']))

