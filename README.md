# Fibonacci Web Service
**Challenge:**

```Create a web service that accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0```

1. The project should provide a RESTful web service.

  a. The web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. 
  
  I.E. given n  = 5, appropriate output would represent the sequence [0, 1, 1, 2, 3].

  b. Given a negative number or non integer, respond with an appropriate error.

2. Include whatever instructions are necessary to build and deploy/run the project, where "deploy/run" means the web service is accepting requests and responding to them as appropriate.

Issued from the location where you downloaded the project. The service will be
available on port ``8080`` of your host operating system, eg::

  ``http://localhost:8080/fibonacci/<n>``

NOTE: 
    **Approach this as representing a more complex problem that you'll have to put into production and maintain for 5 years.**

Thoughts about a production web service:
```
1) Security
      * encryption
2) Performance
      * calculate the full sequence every time, or store sequences that are already called?
      * Right now, n is not limited. A user can enter large number which can cause memory issues
3) Scalability-
      * Load balancer
      * Ability to scale out number of web servers
4) High availability
      * Handled by application layer or VM infrastructure?
5) Monitoring / Alerting in case web service is unavailable
6) Dependencies
      * Python- future upgrades
      * Combined with other web services?
```

```
Helpful Web links:
    * Fibonacci code performance considerations: http://mortada.net/fibonacci-numbers-in-python.html
    * Python error handling: https://docs.python.org/2/tutorial/errors.html
```
