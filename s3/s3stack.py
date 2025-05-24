from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
)
from constructs import Construct

class MyS3Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the S3 bucket
        bucket = s3.Bucket(
            self,
            "MyFirstBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,  # Delete bucket on `cdk destroy`
            auto_delete_objects=True               # Required to auto-delete contents
        )
