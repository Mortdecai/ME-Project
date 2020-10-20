#! /bin/sh

#[ ! -f ./bin/builder ] || mkdir ./bin/builder
#./dist/builder ./doc ./ME-Project.docx
./builder/src/builder.py ./doc ./ME-Project.docx
