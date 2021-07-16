#!/bin/bash

VAR=$( systemctl status mysql  2> /dev/null | grep -c "active (running)" ) 
if [[ $VAR == 0 ]]; then
    exit 1
fi

VAR=$( systemctl status ssh  2> /dev/null | grep -c "active (running)" ) 
if [[ $VAR == 0 ]]; then
    exit 1
fi

VAR=$( systemctl status ruina  2> /dev/null | grep -c "active (running)" ) 
if [[ $VAR == 0 ]]; then
    exit 1
fi

exit 0