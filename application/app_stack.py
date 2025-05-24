from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy
)
from constructs import Construct

class AppStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        s3.Bucket(self, 
            "MyFirstBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY
        )
