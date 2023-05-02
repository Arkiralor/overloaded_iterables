#!/bin/sh

count_iterations=0

while [$count_iterations -lt 10]
do
    python -m pytest tests -v --html=.pytest_cache/report.html --capture sys -rP -rF
    $count_iterations=`expr $acount_iterations + 1`
done