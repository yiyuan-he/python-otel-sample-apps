# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import Flask, request

# Let's use Amazon S3
kinesis_client = boto3.client("kinesis")

app = Flask(__name__)


@app.route("/server_request")
def server_request():
    print(request.args.get("param"))
    stream_name = "yiyuanh-test-otel-stream"
    consumer_name = "test-consumer"
    stream_arn = "arn:aws:kinesis:us-west-2:445567081046:stream/yiyuanh-test-otel-stream"
    # kinesis_client.register_stream_consumer(
    #     StreamARN=stream_arn,
    #     ConsumerName=consumer_name
    # )
    # kinesis_client.describe_stream(StreamName=stream_name)
    kinesis_client.describe_stream_consumer(StreamARN=stream_arn, ConsumerName=consumer_name)
    return "served"


if __name__ == "__main__":
    app.run(port=8082)
