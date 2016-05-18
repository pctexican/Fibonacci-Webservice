RESTful Web Service 
===================

**RESTful web service example in PYTHON.**

Dependencies:
---

* **Python 2.7 or higher**
* web.py module
  * `sudo pip install web.py`
* Apache Tomcat

Start service
---

Use the following command to start service on default port 8080 from the location where you downloaded the project: 
`python main.py`

The service by default will be available on port ``8080`` of your host operating system, for example:

  ``http://localhost:8080/fibonacci/<n>``
  
Usage
---

The following URL will take you to the homepage:
`http://localhost:8080/`

To generate the Fibonacci series, the URL is:
`localhost:8080/fibonacci/n`

