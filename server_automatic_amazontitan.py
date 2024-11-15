# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import boto3
import json
from flask import Flask, request

# Let's use Amazon S3
client = boto3.client("bedrock-runtime")

app = Flask(__name__)

@app.route("/server_request")
def server_request():
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    model_id = "amazon.titan-text-premier-v1:0"
    prompt = "Which LLM are you?"
    native_request = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 512,
            "temperature": 1,
            "topP": 0.7,
        },
    }

    request = json.dumps(native_request)
    try:
        # Invoke the model with the request.
        response = client.invoke_model(modelId=model_id, body=request)
        raw_response = response.get('body').read()
        decoded_response = raw_response.decode('utf-8')
        response_body = json.loads(decoded_response)
        completion_text = response_body['results'][0]['outputText']
        print("Completion text:", completion_text)
    except (Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        exit(1)

    return ""

if __name__ == "__main__":
    app.run(port=8082)
