from aws_cdk import (
    Stack,
    SecretValue,
    pipelines as pipelines,
)
from constructs import Construct
from Pipeline.pipeline_stage import ApplicationStage

class PipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        source = pipelines.CodePipelineSource.git_hub(
            "BanksBytes/CDKProject",
            "main",
            authentication=SecretValue.secrets_manager("GITHUB_TOKEN")
        )

        synth = pipelines.ShellStep("Synth",
            input=source, 
            commands=[
               # "npm install -g aws-cdk",
                "python -m venv .venv",
                ". .venv/bin/activate",
                "pip install -r requirements.txt",
                "cdk synth"
            ]
        )

        pipeline = pipelines.CodePipeline(self, "Pipeline", synth=synth)

        deploy_stage = ApplicationStage(self, "DeployAPP")
        pipeline.add_stage(deploy_stage)
