#!/bin/bash

git pull
git add .
git commit -m "Added back ability to disable environment check and check-plot"
git tag -a v3.3 -m "Version 3.3"
git push
git push origin v3.3
