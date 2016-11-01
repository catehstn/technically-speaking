#!/bin/bash

TMP_FILE="tmp.html"
url=$1

curl -Ls -o ${TMP_FILE} ${url}
title=`awk -vRS="</title>" '/<title>/{gsub(/.*<title>|\n+/,"");print;exit}' ${TMP_FILE}`
rm -f ${TMP_FILE}

title=`echo ${title} | sed -e 's/^The Eloquent Woman: //'`
title=`echo ${title} | sed -e 's/ . Medium$//'`

echo ${title}
