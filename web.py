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