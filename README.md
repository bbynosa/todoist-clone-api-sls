## Run at local environment
1. Install Serverless Framework on your machine:
``` cli
npm install -g serverless
```
2. Install project dependencies (for serverless, not for python code):
``` cli
npm install
```
3. Install DynamoDB local (separately):
``` cli
sls dynamodb install
```
4. Start local DynamoDB table and seed:
 ``` cli
sls dynamodb start
```
5. Start local API:
```cli
sls offline
```

## TODOs
- store lambda code on src/ directory (DONE)
- local environment variables on sls yml
- least privilege principle on cfn execution role
- use ssm param store
- test installing python dependencies (requirements.txt) on codebuild
- migrate API framework from AWS Lambda functions to Django RF? (sls offline doesn't offer local step-through debugging)

