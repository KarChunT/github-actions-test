#!/bin/sh

# if [ true ]
# then
#     echo 'error'
#     exit 1
# fi

# debug message
echo "::debug::Debug message"
echo "::warning::Warning message"
echo "::error::error message"

# set secret
echo "::add-mask::$1"
echo "Hello $1"
time=$(date)
# set output
echo "::set-output name=time::$time"

# grouping
echo "::group::Some expandable logs"
echo "some stuff"
echo "good"
echo "::endgroup::"

# set env value
echo "::set-env name=HELLO::envvalue"