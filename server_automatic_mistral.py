import boto3
import json
from flask import Flask, request

app = Flask(__name__)
client = boto3.client("bedrock-runtime", region_name="us-east-1")

@app.route("/server_request")
def server_request():
    model_id = "mistral.mistral-large-2402-v1:0"
    prompt = "Describe the difference between a compiler and interpreter in one line"

    instruction = "<s>[INST] {{prompt}} [/INST]\n".replace("{{prompt}}", prompt)

    request_body = {
        "prompt": instruction,
        "max_tokens": 4096,
        "temperature": 0.75,
        "top_p": 0.25
    }

    try:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        response_body = json.loads(response.get("body").read())
        completion_text = response_body["outputs"][0]["text"]
        print("Completion text:", completion_text)
    except Exception as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")

    return ""

if __name__ == "__main__":
    app.run(port=8082)
