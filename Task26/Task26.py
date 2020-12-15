from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            number = self.get_number()
        except Exception:
            self.send_response(400)
            message = ''
        else:
            is_prime_str = 'true' if self.is_prime(number) else 'false'
            message = f'{{"number":{number},"is_prime":{is_prime_str}}}'
            self.send_response(200)

        self.protocol_version = "HTTP/1.1"
        self.send_header("Content-Length", len(message))
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))
        print(urllib.parse.parse_qs(self.path[2:]))
        return

    def get_number(self):
        params = urllib.parse.parse_qs(self.path[9:])
        number = params["number"][0]
        number = int(number)
        return number

    def is_prime(self, number):
        for i in range (2, number):
            if number % i == 0:
                return False
        return True

def run():
    server = ('', 8080)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    run()

