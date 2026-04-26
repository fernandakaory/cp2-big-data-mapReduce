#!/bin/bash

awk '
{
  count[$1] += $2
}
END {
  for (word in count)
    print word "\t" count[word]
}'