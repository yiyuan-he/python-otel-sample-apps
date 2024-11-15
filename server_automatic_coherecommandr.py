import boto3
import json
from flask import Flask, request

app = Flask(__name__)
client = boto3.client("bedrock-runtime", region_name="us-east-1")

@app.route("/server_request")
def server_request():
    model_id = "cohere.command-r-plus-v1:0"
    prompt = "Convince me to write a LISP interpreter in one line"
    request_body = {
        "message": prompt,
        "max_tokens": 4096,
        "temperature": 1,
        "p": 0.75
    }

    try:
        # Invoke the model
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        ) 
        response_body = json.loads(response.get("body").read())
        completion_text = response_body["text"]
        print("Completion text:", completion_text)
    except Exception as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")

    return ""

if __name__ == "__main__":
    app.run(port=8082)
