#!/bin/bash
echo "--- test 1 ---"
echo "get-people"
python3 main.py get-people

echo "--- test 2 ---"
echo "get-drinks"
python3 main.py get-drinks

echo "--- test 3 ---"
echo "get-peopl"
python3 main.py get-peopl

echo "--- test 4 ---"
echo "get-people get-drinks"
python3 main.py get-people get-drinks