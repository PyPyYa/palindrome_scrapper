# English Palindrome Scrapper

Creates a JSON document with all of the English palindromes avaiable from Wikipedia. This document was created to test a palindrome detection function.

To run:

* Install virtualenv via pip

```
    pip install virtualenv
```

* Create a virtual environment for the project

```
    cd project_folder
    virtualenv venv
```

* Activate the virtual environment

```
    source venv/bin/activate
```

* Run the spider

```
    scrapy runspider palindrome.py -o words.json
```

The JSON output will be encoded with utf-8.