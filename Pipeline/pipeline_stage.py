from aws_cdk import Stage
from constructs import Construct
from application.app_stack import AppStack

class ApplicationStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        AppStack(self, "AppStack")
