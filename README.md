## Install project dependencies
1. Serverless framework globally
``` cli
npm install -g serverless
```
2. Npm packages for Serverless
``` cli
npm install
```
3. Setup python project virtual environment (venv)
``` cli
python3 -m venv .venv
```
4. Activate venv (for Windows)
``` cli
.venv\Scripts\activate.bat
```
5. Python project dependencies
``` cli
pip install -r requirements.txt
```
6. DynamoDB local
``` cli
sls dynamodb install
```

## Run at local environment
1. Start local DynamoDB table and seed:
 ``` cli
sls dynamodb start
```
2. Start local API:
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

