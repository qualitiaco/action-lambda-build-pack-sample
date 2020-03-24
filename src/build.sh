#!/bin/bash -ex

OUTPUT_PATH=${OUTPUT_PATH:-output}

# ** If you want, you can compile from source
#
# yum install -y curl-devel expat-devel wget openssl-devel
# wget 'https://github.com/git/git/archive/v2.26.0.tar.gz'
# tar xvzf v2.26.0.tar.gz
# cd git-2.26.0
# make configure
# ./configure
# make
# make install

yum install -y git

cp -a /usr/bin/git ${OUTPUT_PATH}
cp -a /usr/libexec/git-core/git-remote-https ${OUTPUT_PATH}
cp -a /usr/libexec/git-core/git-remote-http ${OUTPUT_PATH}
