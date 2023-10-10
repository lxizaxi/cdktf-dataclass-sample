#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from imports.terraform_aws_modules.aws import Vpc


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here
        AwsProvider(self, "Aws", region="ap-northeast-1")

        Vpc(
            self,
            "vpc-from-cdk-for-terraform",
            name="vpc-from-cdk-for-terraform",
            cidr="10.0.0.0/16",
            azs=["ap-northeast-1a", "ap-northeast-1c", "ap-northeast-1d"],
            public_subnets=["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"],
        )


app = App()
MyStack(app, "cdktf-dataclass-sample")

app.synth()
