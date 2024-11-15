# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import Flask, request

# Let's use Amazon S3
bedrock_client = boto3.client("bedrock")

app = Flask(__name__)


@app.route("/server_request")
def server_request():
    print(request.args.get("param"))
    guardrail_id = "ml2x8svlammy"
    bedrock_client.get_guardrail(guardrailIdentifier=guardrail_id)
    return "served"


if __name__ == "__main__":
    app.run(port=8082)
