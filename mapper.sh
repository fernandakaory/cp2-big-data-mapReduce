#!/bin/bash

while read line
do
  echo "$line" \
  | tr ' ' '\n' \
  | grep -v '^$' \
  | awk '{print $1"\t1"}'
done