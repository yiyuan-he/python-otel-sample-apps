# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import Flask, request

# Let's use Amazon S3
dynamodb_client = boto3.client("dynamodb")

app = Flask(__name__)


@app.route("/server_request")
def server_request():
    print(request.args.get("param"))
    table_name = "yiyuanh-test-otel-table"
    dynamodb_client.describe_table(TableName=table_name)
    return "served"


if __name__ == "__main__":
    app.run(port=8082)
