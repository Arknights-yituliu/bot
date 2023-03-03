#!/bin/bash

./server.py &
sleep 1
./screenshot.py
kill %1
