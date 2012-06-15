#!/bin/sh

cd /var/cache/motion
wget "http://10.0.0.129:7079/index.php?view=request&request=image&entity=monitor&id=1" -O lastsnap.jpg.tmp
if [ $? -eq 0 ]; then mv lastsnap.jpg.tmp lastsnap.jpg; fi
~/historybands2.py history.png lastsnap.jpg
