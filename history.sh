#!/bin/sh

cd /var/cache/motion
wget "http://10.0.0.129:7079/index.php?view=request&request=image&entity=monitor&id=3" -O lastsnap.jpg.tmp >/dev/null 2>/dev/null
WGET=$?
if [ $WGET -eq 0 ]; then if ! cmp -s lastsnap.jpg.tmp lastsnap.jpg; then mv lastsnap.jpg.tmp lastsnap.jpg; else echo "It's the same pic!"; fi; else echo "Download of new snapshot failed!";fi
~/historybands2.py history.png lastsnap.jpg
