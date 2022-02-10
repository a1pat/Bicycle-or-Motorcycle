# FIRST lambda function


import json
import boto3
import base64


def lambda_handler(event, context):
    '''
    A function to serialize target data from S3
    '''
    
    # get the s3 address from the step function event input
    key = event['s3_key']
    bucket = event['s3_bucket']
    
    # download the data from s3 to /tmp/image.png
    # modeled after HelloBlazePreprocessLambda.py
    s3 = boto3.client('s3')
    s3.download_file(bucket, key, '/tmp/image.png')
    
     # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())
    
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
            }
            
    }




# SECOND lambda function


import json
import base64

# reference: https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/
# reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html
# reference: various discussions in Mentor Help

import boto3

ENDPOINT = 'image-classification-2022-02-09-04-23-37-154'
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    
    '''
    responsible for the classification part - we're going to take the image output from the previous function, decode it, and then pass inferences back to the the Step Function
    '''
    print(event.keys())

    # decode the image data
    image = base64.b64decode(event['body']['image_data'])

    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType='image/png', Body=image)

    
    inferences = response['Body'].read().decode('utf-8')
    
    print(inferences)
    print(type(inferences))

    
    return {
        'statusCode': 200,
        'body': {
            "image_data": event['body']['image_data'],
            "s3_bucket": event['body']['s3_bucket'],
            "s3_key": event['body']['s3_key'],
            "inferences": inferences
            }
        }




# THIRD lambda function

import json

THRESHOLD = 0.99

def lambda_handler(event, context):
    '''
    filter low-confidence inferences
    '''
    
    # get the inferences from the event
    inferences = event['body']['inferences']

    # check if any of the values meets the threshold
    probs = [float(x) for x in inferences[1:-1].split(',')]
    meets_threshold = (max(probs) >= THRESHOLD)

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': {
            "image_data": event['body']['image_data'],
            "s3_bucket": event['body']['s3_bucket'],
            "s3_key": event['body']['s3_key'],
            "inferences": event['body']['inferences']
            }
            
    }
    
