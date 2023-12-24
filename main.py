from phew import access_point, logging, server, dns
from phew.template import render_template
from os import stat

SSID = "Samizdat"
DOMAIN = "sa.miz.dat"
HTDOCS = "htdocs"

@server.route("/hotspot-detect.html", methods=["GET"])
@server.route("/generate_204", methods=["GET"])
@server.route("/redirect", methods=["GET"])
def hotspot(request):
    logging.info("redirecting hotspot request " + request.path)
    return server.redirect(f"http://{DOMAIN}/", 302)

@server.route("/ncsi.txt", methods=["GET"])
@server.route("/connecttest.txt", methods=["GET"])
def hotspot(request):
    return "", 200

@server.route("/", methods=['GET'])
def index(request):
    logging.info("retrieving index.html")
    return render_template(HTDOCS + "/index.html")

@server.route("/data.html", methods=["GET"])
def hotspot(request):
    logging.info("Got data: " + request.query_string)
    return render_template(HTDOCS + "/index.html")

@server.route("/log.txt", methods=["GET"])
def hotspot(request):
    return render_template("log.txt")

@server.catchall()
def catch_all(request):
    try:
        stat(HTDOCS + request.path)
        return render_template(HTDOCS + request.path)
    except OSError:
        return "Not found:" + request.path, 404

ap = access_point(SSID)
ip = ap.ifconfig()[0]
logging.info(f"starting DNS server on {ip}")
dns.run_catchall(ip)
server.run()

