#!/usr/bin/python

import os,sys
import time

import Image
import ImageChops
import ImageDraw
import ImageFont
import historybands2

def main():
    if len(sys.argv) != 3:
        print "Usage: %s history.png input.jpg" % sys.argv[0]
        sys.exit(1)
    historyfile = sys.argv[1]
    infile = sys.argv[2]
    xsize=639
    minute = time.localtime()[4]

    try:
        history = Image.open(historyfile)
        newhistory = ImageChops.offset(history,0,20)
    except:
        newhistory = Image.new("RGB",(640,300))

    last_time = os.stat(infile).st_mtime
    dtime = time.time() - last_time
    dmins = int(round(dtime / 60.0))
    font = ImageFont.load_default()
    newday = Image.open(infile)
    newday = historybands2.shift(newday, dmins)
    newcol = Image.new("RGB",(1440,46))
    newcol.paste(newday.crop((0,165,360,211)),(0,0))
    newcol.paste(newday.crop((0,110,360,156)),(360,0))
    newcol.paste(newday.crop((0,55,360,101)),(720,0))
    newcol.paste(newday.crop((0,0,360,46)),(1080,0))
    newcol = newcol.resize((625,20),Image.ANTIALIAS)
    newhistory.paste(newcol,(15,0))

    draw = ImageDraw.Draw(newhistory)
    draw.rectangle([(0,280),(641,301)], fill=0)
    draw.rectangle([(0,0),(15,20)], fill=0)
    draw.text((1,5), time.strftime("%d",time.localtime(time.time()-(3600*24))), font=font)
    for t, o in zip(range(0,19,6),range(15,600,156)):
        draw.text((o,280), "%02d" % t, font=font)
    draw.text((620,280), "23", font=font)
    draw.text((10,290), time.ctime(), font=font)

    newhistory.save(historyfile)

if __name__ == '__main__':
    main()
