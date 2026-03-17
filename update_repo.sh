#!/bin/bash

git pull
git add .
git commit -m "Update Readme"
git tag -a v3.2 -m "Version 3.2"
git push
git push origin v3.2