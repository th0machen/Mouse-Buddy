from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from mouse_controller import start_mouse, stop_mouse


class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        if self.path == "/start":

            content_length = int(
                self.headers.get("Content-Length", 0)
            )

            body = self.rfile.read(content_length)

            data = json.loads(body)

            duration = int(data.get("duration", 60))

            print(
                f"START command received for {duration} seconds"
            )

            start_mouse(duration)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(
                b'{"status": "started"}'
            )

        elif self.path == "/stop":

            print("STOP command received!")

            stop_mouse()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(
                b'{"status": "stopped"}'
            )

        else:

            self.send_response(404)
            self.end_headers()


server = HTTPServer(
    ("localhost", 5000),
    RequestHandler
)


print("Mouse Buddy controller started")
print("Listening on http://localhost:5000")


server.serve_forever()