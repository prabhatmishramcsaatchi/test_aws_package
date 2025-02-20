import json
import pandas as pd
import numpy as np

def lambda_handler(event, context):
    a=10
    b=20    
    print(a+b)
    print("Done")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
