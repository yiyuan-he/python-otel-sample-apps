import boto3
import json
from flask import Flask, request

app = Flask(__name__)
client = boto3.client("bedrock-runtime", region_name="us-east-1")

@app.route("/server_request")
def server_request():
    model_id = "meta.llama3-70b-instruct-v1:0"
    prompt = "Describe the purpose of a 'hello world' program in one line"

    instruction = (
        "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n"
        "{{prompt}} <|eot_id|>\n"
        "<|start_header_id|>assistant<|end_header_id|>\n"
    ).replace("{{prompt}}", prompt)

    request_body = {
        "prompt": instruction,
        "max_gen_len": 128,
        "temperature": 0.1,
        "top_p": 0.9
    }

    try:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        response_body = json.loads(response.get("body").read())
        completion_text = response_body["generation"]
        print("Completion text:", completion_text)
    except Exception as e:
        print(f"ERROR: Can't invoke {model_id}. Reason: {e}")

    return ""

if __name__ == "__main__":
    app.run(port=8082)
