#!/bin/bash
conda activate main
pip install --upgrade twine
echo "Did you change git action and updated the package?"
read
git status
read
git pull
read
rm dist/*
python setup_version.py
python setup.py sdist bdist_wheel
read
git add --all
git status
read
read -p commit_name="Please, make up the commit name:"
tag=`cat tag_name`
git commit -m $commit_name
read
git tag $tag
read
git push
read
git push --tags
read
twine upload --repository phigaro dist/*
read