#!/bin/bash
aocd > in.txt
head in.txt
echo "# of lines in the input: $(wc -l in.txt)"