#! /bin/sh

python3 -m pip install -r ./auto/builder/requirements.txt
python3 ./auto/builder/src/builder.py ./auto/ME-Project.docx.builder
