import subprocess


def start_camera_feed():
    p = subprocess.Popen(
        "/opt/vc/bin/raspivid -o - -t 0 -hf -vf -w 640 -h 360 -fps 25|cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h26",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return p
