import boto3
import json
from flask import Flask, request

app = Flask(__name__)
client = boto3.client("bedrock-runtime", region_name="us-east-1")

@app.route("/server_request")
def server_request():
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    prompt = "Which LLM are you?"
    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": [{
                    "type": "text",
                    "text": prompt
                }]
            }
        ],
        "temperature": 1,
        "top_p": 1 
    }

    try:
        # Invoke the model
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        response_body = json.loads(response.get("body").read())
        completion_text = response_body["content"][0]["text"]
        print("Completion text:", completion_text)

    except Exception as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")

    return ""

if __name__ == "__main__":
    app.run(port=8082)
