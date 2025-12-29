# itech210-recap

1) create your git ignore file
1.1) in the file explorer blade, right click > new file > ".gitignore"

2) create your virtual environment
2.1) in your terminal run the command: py -m venv env
2.2) activate your virtual environment with the command: env\Scripts\Activate
2.2.1) it is properly activated if you see (env) in your terminal before your path
2.3) add env/ and .env/ to your git ignore file

3) requirements txt
3.1)use the command: pip freeze > requirements.txt
3.1.1) this captures all of your imports and requirements and puts them in the requirements.txt file
3.2) use the command: pip install -r requirements.txt
3.2.1) this installs all of the requirements needed from the requirements.txt file
 