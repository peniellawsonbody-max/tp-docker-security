from flask import Flask, request
import subprocess

app = Flask(__name__)

# Endpoint d'administration vulnérable
# (NE PAS UTILISER EN PROD)
@app.route("/admin/run", methods=["POST"])
def run_cmd():
    cmd = request.form.get("cmd", "")
    if not cmd:
        return "No cmd", 400
    # Exécution directe - vulnérabilité volontaire
    out = subprocess.getoutput(cmd)
    return out, 200

@app.route("/")
def index():
    return "Vuln demo"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
