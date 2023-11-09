from flask import Flask, render_template
import psutil

app = Flask(__name__)


@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "The CPU utilization or Memory Utilization is too high!"
    return render_template(
        "index.html", cpu_util=cpu_metric, mem_util=mem_metric, message=Message
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
