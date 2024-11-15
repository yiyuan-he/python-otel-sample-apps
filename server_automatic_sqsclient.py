# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import Flask, request

# Let's use Amazon S3
sqs_client = boto3.client("sqs")

app = Flask(__name__)


@app.route("/server_request")
def server_request():
    print(request.args.get("param"))
    queue_url = "https://sqs.us-west-2.amazonaws.com/445567081046/yiyuanh-test-otel-queue"
    # sqs_client.get_queue_attributes(QueueUrl=queue_url)
    sqs_client.create_queue(QueueName="yiyuanh-test-create-sqs-queue-1")
    return "served"


if __name__ == "__main__":
    app.run(port=8082)
