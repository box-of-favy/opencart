import json
from browsermobproxy import Server
import os
import psutil

BROWSERMOB_PROXY_PATH = (r"C:\Users\favy\Documents\work\browsermob-proxy-2.1.4\bin"
                         r"\browsermob-proxy.bat")


def start_proxy_session(session_dir, port):
    """
    Starts the BrowserMob Proxy server on the given port and sets up logging to the session
    directory.

    :param session_dir: Directory where log files should be saved.
    :param port: Port for BrowserMob Proxy to listen on (default 8081).
    :return: Proxy instance.
    """
    log_file = os.path.join(session_dir, "server.log")

    server = Server(BROWSERMOB_PROXY_PATH, options={"port": port, "trustAllServers": "true"})
    server.start()  # Start proxy on custom port
    proxy = server.create_proxy()  # Create the proxy instance

    # Start capturing HTTP traffic and log to session directory
    har_file_path = f"{session_dir}/opencart_test.har"
    proxy.new_har("opencart_test")  # Start capturing traffic

    return proxy, server, har_file_path


def stop_proxy(proxy, server, har_file_path):
    har_data = proxy.har
    with open(har_file_path, "w") as har_file:
        json.dump(har_data, har_file)
    if proxy:
        proxy.close()
    if server:
        server.stop()

    for proc in psutil.process_iter(['pid', 'name']):
        for conn in proc.connections(kind='inet'):
            if conn.laddr.port in [8081, 8082]:
                proc.kill()