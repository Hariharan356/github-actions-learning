
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class Handler(SimpleHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            file_path = Path("templates/index.html")

            content = file_path.read_bytes()

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(content)

        else:
            super().do_GET()


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)

    print("Server running on port 8000")

    server.serve_forever()
