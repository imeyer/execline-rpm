#!/bin/sh

# Now I know this is going to seem *INSANE* to you. It is.
# Set HOME to $(pwd) so that this repo's .rpmmacros is read
# as though it was in the real $HOME
HOME=$(pwd)

cd $HOME/SPECS
rpmbuild -ba execline.spec
