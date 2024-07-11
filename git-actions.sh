#!/bin/sh

#
#	Git-actions by LiddulBOFH
#
#	To be called before the server actually starts, but after the start script is fired off
#

python3 autopull.py "$PWD/garrysmod/addons"