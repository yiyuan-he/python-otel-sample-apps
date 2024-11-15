# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import Flask, request

# Let's use Amazon S3
lambda_client = boto3.client("lambda")

app = Flask(__name__)


@app.route("/server_request")
def server_request():
    print(request.args.get("param"))
    function_arn = "arn:aws:lambda:us-west-2:445567081046:function:yiyuanh-test-otel-lambda"
    function_name = "yiyuanh-test-otel-lambda"
    event_source_mapping_uuid = "a7f25f34-ad44-480f-8385-4c0affee4d1b"
    lambda_client.get_function(FunctionName=function_arn)
    # lambda_client.get_event_source_mapping(
    #     UUID=event_source_mapping_uuid
    # )
    return "served"


if __name__ == "__main__":
    app.run(port=8082)
