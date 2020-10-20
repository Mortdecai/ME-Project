#! /bin/sh

#sudo pyinstaller --onefile ./src/builder.py
#cxfreeze ./src/builder.py --target-dir ./bin
cxfreeze setup.py --target-dir=./bin --target-name=builder

#mv ./dist/builder ./bin
#[ ! -d ./build ] || rm -r ./build
#[ ! -d ./dist ] || rm -r ./dist
#[ ! -d ./src/__pycache__ ] || rm -r ./src/__pycache__
#rm ./builder.spec
