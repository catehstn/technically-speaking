#!/usr/bin/python

from __future__ import print_function

import HTMLParser
import os
import re
import subprocess
import sys
import urllib

AUTHOR = re.compile('\[@([^\]]+)\]')
TWEET_IT = re.compile('\[\[(.+)\]\((.+)\)\]\[(tweet it)\]')

def main(argv):
  input_filename = argv[1]
  output_filename = input_filename + '.tmp'

  output_fp = open(output_filename,'w')
  get_title_sh = os.path.join(os.path.dirname(argv[0]), 'get-title.sh')

  with open(input_filename) as f:
    for line in f:
      m = TWEET_IT.search(line)
      if m:
        text = m.group(1)
        link = m.group(2)

        title = subprocess.check_output([get_title_sh, link])
        title = HTMLParser.HTMLParser().unescape(title.strip())

        author = None
        author_m = AUTHOR.search(line)
        if author_m:
          author = author_m.group(1)

        tweet = ''
        if link.find('twitter.com') == -1:
          tweet = title
          if author is not None:
            tweet += ' by @' + author
          tweet += ' ' + link + ' via @techspeakdigest'
        else:
          tweet = 'via @techspeakdigest ' + link

        sys.stderr.write(link)
        url = 'https://twitter.com/home?status=' + urllib.quote(tweet.encode('utf8'))

        replacement = '[[' + text + '](' + link + ')][[tweet it](' + url + ')]'
        output_fp.write(line.replace(m.group(0), replacement))

        sys.stderr.write('... Done\n')
      else:
        output_fp.write(line)

    output_fp.close()
    os.rename(output_filename, input_filename)


if __name__ == '__main__':
  main(sys.argv)
