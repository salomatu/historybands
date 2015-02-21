#!/usr/bin/python

import os,sys
import time

import Image
import ImageChops
import ImageDraw
import ImageFont

def main():
    if len(sys.argv) != 3:
        print "Usage: %s history.png input.jpg" % sys.argv[0]
        sys.exit(1)
    historyfile = sys.argv[1]
    infile = sys.argv[2]
    xsize=359
    ysize=229
    minute = time.localtime()[4]
#    shit = sys.stdin.read()

    try:
        history = Image.open(historyfile)
        last_time = os.stat(historyfile).st_mtime
    except:
        history = Image.new("RGB",(xsize+1,ysize+1))
        last_time = time.time()

    dtime = time.time() - last_time
    dmins = int(round(dtime / 60.0))
    sourcedtime = time.time() - os.stat(infile).st_mtime
    font = ImageFont.load_default()

    history = shift(history, dmins)
    if sourcedtime < 60: 
        newcol = Image.open(infile).resize((60,45),Image.ANTIALIAS)
        history.paste(newcol.crop((minute,0,minute+1,45)),(xsize,0))

    draw = ImageDraw.Draw(history)
    draw.line([(xsize,45),(xsize,54)], fill="#000000", width=1)
    if not minute:
        draw.line([(xsize,36),(xsize,45)], fill="#25754F", width=1)
    elif (minute % 10) == 0:
        draw.line([(xsize,44),(xsize,45)], fill="#25754F", width=1)
    else:
        draw.line([(xsize,45),(xsize,45)], fill="#25754F", width=1)
    if minute == 10:
        draw.text((xsize-16,45), time.strftime("%H"), font=font, fill="#25754F")

    draw.rectangle([(0,ysize-9),(xsize+1,ysize+1)], fill=0)
    draw.text((10,ysize-9), time.ctime(), font=font, fill="#25754F")

    history.save(historyfile)

def shift(history, dist):
    if dist < 1:
        return history
    if dist > 1440:
        dist = 1440
    while dist > 0:
        if dist > 360:
            cutdist = 360
        else:
            cutdist = dist
        history = ImageChops.offset(history,-cutdist,0)
        shiftblock = history.copy().crop((360-cutdist,0,360,165))
        history.paste(shiftblock,(360-cutdist,55))
        draw = ImageDraw.Draw(history)
        draw.rectangle([(360-cutdist,0),(360,54)], fill="#0000FF")
        dist -= cutdist
    return history

if __name__ == '__main__':
    main()
