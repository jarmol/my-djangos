my-djangos
==========

Learning Python Django with Debian 6 Linux (Squeeze, old stable)

1. Go to the project directory my-djangos/mysite.
2. Start your server:    ./manage.py runserver
3. Open in your browser: http://127.0.0.1:8000/
............................

Run example

@nc10:~/mydjangos/my-djangos$ cd mysite/  
@nc10:~/mydjangos/my-djangos/mysite$ ./manage.py runserver  
Validating models...  
0 errors found

Django version 1.2.3, using settings 'mysite.settings'  
Development server is running at http://127.0.0.1:8000/  
Quit the server with CONTROL-C.  
[17/Oct/2014 21:24:47] "GET / HTTP/1.1" 200 125  
[17/Oct/2014 21:24:56] "GET /hello HTTP/1.1" 301 0  
[17/Oct/2014 21:24:56] "GET /hello/ HTTP/1.1" 200 342  
[17/Oct/2014 21:25:01] "GET /index/ HTTP/1.1" 200 125  
[17/Oct/2014 21:25:03] "GET /time HTTP/1.1" 301 0  
[17/Oct/2014 21:25:03] "GET /time/ HTTP/1.1" 200 150  
[17/Oct/2014 21:25:06] "GET /index/ HTTP/1.1" 200 125  
[17/Oct/2014 21:25:08] "GET /time/plus/3 HTTP/1.1" 301 0  
[17/Oct/2014 21:25:08] "GET /time/plus/3/ HTTP/1.1" 200 111  
[17/Oct/2014 21:26:21] "GET /time/plus/2/ HTTP/1.1" 200 111  
[17/Oct/2014 21:26:26] "GET /index/ HTTP/1.1" 200 125  
^C@nc10:~/mydjangos/my-djangos/mysite$ 
// Server stopped using Ctrl-C
