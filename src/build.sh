#!/bin/bash -ex

OUTPUT_PATH=${OUTPUT_PATH:-output}

yum install -y git
cp -a /usr/bin/git ${OUTPUT_PATH}
