# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer,BaseHTTPRequestHandler
content='''
<html lang="en">
<head>
    <title>lap specs.</title>
</head>
<body>

     <table border="3" cellpadding="10">
        <caption style="font-size: x-large;">LAPTOP SPECIFICATTION</caption>
        <TR>
            <TD>BRAND</TD>
            <TD>LENOVO</TD>
        </TR>
        <TR>
            <TD>SERIES</TD>
            <TD>THINKPAD E16 GEN1</TD>
        </TR>
        <TR>
            <TD>PROCESSOR BRAND</TD>
            <TD>INTEL</TD>
        </TR>
        <TR>
            <TD>PROCESSOR TYPE</TD>
            <TD>CORE I5</TD>
        </TR>
        <TR>
            <TD>GRAPHICS CARD INTERFACE</TD>
            <TD>INTEGRATED</TD>
        </TR>
        <TR>
            <TD>OPERATING SYSTEM</TD>
            <TD>WINDOWS 11 HOME</TD>
        </TR>
     </table> 
</body>
</html>
'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
```


## OUTPUT:
![Screenshot 2025-04-29 140046](https://github.com/user-attachments/assets/cd491d8d-c28c-4368-9827-b1782e929df9)
![Screenshot 2025-04-29 135618](https://github.com/user-attachments/assets/955a276d-3718-4475-991f-cc68cabb256e)



## RESULT:
The program for implementing simple webserver is executed successfully.
