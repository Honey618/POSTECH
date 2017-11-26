# POSTECH
### Setting Virtual Environment to Python3
```
pip3 install virtualenv
virtualenv -p python3 env
```
### CS 408 Computer Science Project
```
source env/bin/activate
pip3 install -r requirements.txt  
```
### Installing Semantic-UI
```
brew install node
npm install -g gulp
cd POSTECH/static/
npm install semantic-ui --save
cd semantic/
gulp build
```
### To test google OCR library
```
cd O2O/parser/  
python3 detect.py text [image path]  
```

ex) python3 detect.py text test1.jpeg

### If you've downloaded new package.
```
pip freeze > requirements.txt
```

