from http.server import HTTPServer, BaseHTTPRequestHandler


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        html = """
        <html>
        <body>
            <h1>Insurance Deployment Demo</h1>
            <h2>Application running on AWS EC2!</h2>
            <p>Calculator Result: 10 + 5 = 15</p>
            <p>Status: Successfully deployed</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Server running on port 8000")
    server.serve_forever()