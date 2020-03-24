# action-lambda-build-pack-sample
This is the sample code for action-lambda-build-pack.

You can find github actions here.

https://github.com/qualitiaco/action-lambda-build-pack

Also you can use as docker,

https://hub.docker.com/r/qualitiaco/build-and-pack


## Directory Structure of this Sample

```
.
|-- .github
|   `-- workflows
|       `-- build.yaml      <-- workflow
|-- README.md               <-- This file
|-- output                  <-- Directory for output
|-- py
|   `-- lambda_function.py  <-- Python script for AWS Lambda
`-- src
    `-- build.sh            <-- Build Script
```


## How to work

When you push to github, this will work.

1. src/build.sh is invoked from workflow. This build.sh will yum git and copy git command and git-remote-http[s] command into output directory.
2. Workflow will check which library will be necessary for those commands and copy them into output/lib directory.
3. Workflow will merge those commands and libraries and python script in to one zip file.
4. Then upload to AWS Lambda as a function.
