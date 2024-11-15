import boto3
import json
from flask import Flask, request

app = Flask(__name__)
client = boto3.client("bedrock-runtime", region_name="us-east-1")

@app.route("/server_request")
def server_request():
    model_id = "ai21.jamba-1-5-mini-v1:0"

    messages = [{
        "role": "user",
        "content": "Which LLM are you?"
    }]

    request_body = {
        "messages": messages,
        "max_tokens": 1000,
        "top_p": 0.8,
        "temperature": 0.7
    }

    try:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        response_body = json.loads(response.get("body").read())
        completion_text = response_body["choices"][0]["message"]["content"]
        print("Completion text:", completion_text)
    except Exception as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")

    return ""

if __name__ == "__main__":
    app.run(port=8082)
