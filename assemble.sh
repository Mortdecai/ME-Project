#! /bin/sh

#[ ! -f ./bin/builder ] || mkdir ./bin/builder
#./dist/builder ./doc ./ME-Project.docx
python3 ./builder/src/builder.py ./doc ./ME-Project.docx
