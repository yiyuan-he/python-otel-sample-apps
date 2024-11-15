# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import boto3
from flask import Flask, request

# Let's use Amazon S3
bedrock_agent_client = boto3.client("bedrock-agent")

app = Flask(__name__)


@app.route("/server_request")
def server_request():
    print(request.args.get("param"))
    agent_id = "ZOBKMTWOZC"
    knowledge_base_id = "VVTY3IRMU6"
    data_source_id = "LXNY6X9NAZ"
    bedrock_agent_client.get_data_source(dataSourceId=data_source_id, knowledgeBaseId=knowledge_base_id)
    return "served"


if __name__ == "__main__":
    app.run(port=8082)
