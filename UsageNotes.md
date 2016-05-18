RESTful Web Service 
===================

**RESTful web service example in PYTHON.**

Dependencies:
---

* **Python 2.7 or higher**
* web.py module
  * `sudo pip install web.py`
* Apache Tomcat
  * `sudo apt-get install apache2`

Start service
---

Use the following command to start service on default port 8080: 
`python main.py`

Issued from the location where you downloaded the project. The service will be
available on port ``8080`` of your host operating system, eg::

  ``http://localhost:8080/fibonacci/<n>``
  
Usage
---

The following URL will take you to the homepage:
`http://localhost:8080/`

To generate the Fibonacci series, the URL is:
`localhost:8080/fibonacci/n`

