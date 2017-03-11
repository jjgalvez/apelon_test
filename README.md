# How to reproduce the error

 1. create a virtual env python3 -m venv <dir>
 2. clone repository:  git clone https://github.com/jjgalvez/apelon_test.git
 3. activate and install dependencies from requirements.txt:  pip install -r requirements.text
 4. run the wsdl server which only returns the wsdl's: python3 wsdlserver.py
 5. run test code, apelontest.py to illustrate the issue

 All wsdls are in the templates folder, and the expected payload from the actual server is envelope.xml
