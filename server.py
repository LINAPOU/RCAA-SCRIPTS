import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from scripts import charger_scripts, reconnaitre_scenario

scripts = charger_scripts("dataset.csv")

class Handler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self._set_headers()
        self.end_headers()

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/reconnaitre":
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            data = json.loads(body.decode("utf-8"))
            saisie = data["actions"]

            actions = [a.strip() for a in saisie.split(";") if a.strip()]
            script_id, scenario, score = reconnaitre_scenario(actions, scripts)

            response = {
                "actions": actions,
                "id": script_id,
                "scenario": scenario,
                "score": round(score, 2)
            }

            self.send_response(200)
            self._set_headers()
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))

server = HTTPServer(("localhost", 8000), Handler)
print("Serveur lancé sur http://localhost:8000")
server.serve_forever()
