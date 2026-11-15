"""Abre a animação da Laura no navegador, como no vídeo do TikTok.

Uso:  python serve.py   (Ctrl+C para parar)

Fotos: coloque até 12 fotos na pasta "fotos", com os nomes 1.jpg, 2.jpg, 3.jpg...
(ou .png). Elas aparecem flutuando em 3D dentro do coração.

Música própria: coloque um arquivo chamado musica.mp3 nesta pasta e ele toca
no lugar da trilha gerada. Para o coração explodir num momento exato da música,
edite CUSTOM_DROP_SECONDS no começo do <script> em laura.html.
"""
import http.server
import socketserver
import threading
import webbrowser
from pathlib import Path

PORT = 8765
ROOT = Path(__file__).resolve().parent
PAGE = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
</head><body style="margin:0">{body}</body></html>"""


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            body = (ROOT / "laura.html").read_text(encoding="utf-8")
            data = PAGE.format(body=body).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        elif self.path == "/musica.mp3" or self.path.startswith("/fotos/"):
            super().do_GET()
        else:
            self.send_error(404)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    (ROOT / "fotos").mkdir(exist_ok=True)
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        url = f"http://127.0.0.1:{PORT}/"
        print(f"💓 Abrindo {url}  (Ctrl+C para parar)")
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nAté a próxima 💓")
