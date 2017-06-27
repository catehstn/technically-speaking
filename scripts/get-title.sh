#!/bin/bash

TMP_FILE="tmp.html"
url=$1

curl -Ls -o ${TMP_FILE} ${url}
title=`cat ${TMP_FILE} | tr -d '\n' | egrep -io '<title>.*</title>' | sed -e 's/<title>//' | sed -e 's/<\/title>//'`
rm -f ${TMP_FILE}

title=`echo ${title} | sed -e 's/^The Eloquent Woman: //'`
title=`echo ${title} | sed -e 's/ &#8211; Accidentally in Code$/ by @catehstn/'`
title=`echo ${title} | sed -e 's/ . Medium$//'`
title=`echo ${title} | sed -e 's/ . GitHub$//'`

echo "${title}"