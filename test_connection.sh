#!/bin/bash
ping $1 -c 1 > null;
if [ $? -eq 0 ]; then
    echo $1 is up;
    echo `iperf -c $1 -t 1| tail -c 16`
else
    echo $1 is down;
fi
