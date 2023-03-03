#!/bin/bash

./server.py &
./screenshot.py
kill %1
