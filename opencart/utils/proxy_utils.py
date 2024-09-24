import json
from browsermobproxy import Server

BROWSERMOB_PROXY_PATH = r"C:\Users\favy\Documents\work\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat"


def start_proxy_session(session_dir, port=8081):
    """
    Starts the BrowserMob Proxy server on the given port and sets up logging to the session directory.

    :param session_dir: Directory where log files should be saved.
    :param port: Port for BrowserMob Proxy to listen on (default 8081).
    :return: Proxy instance.
    """
    server = Server(BROWSERMOB_PROXY_PATH, options={"port": port})
    log_file_path = f"{session_dir}/server.log"
    server.start(options={"port": port, "log_path": session_dir,
                          "log_file": log_file_path})  # Start proxy on custom port
    proxy = server.create_proxy()  # Create the proxy instance

    # Start capturing HTTP traffic and log to session directory
    har_file_path = f"{session_dir}/opencart_test.har"
    proxy.new_har("opencart_test")  # Start capturing traffic

    return proxy, server, har_file_path


def stop_proxy(proxy, server, har_file_path):
    """
    Stops the BrowserMob Proxy server and saves the captured HTTP traffic to a HAR file.

    :param proxy: Proxy instance to stop.
    :param server: Server instance to stop.
    :param har_file_path: Path to the HAR file where HTTP logs should be saved.
    """
    # Capture HTTP requests and save them to the HAR file
    har_data = proxy.har
    with open(har_file_path, "w") as har_file:
        json.dump(har_data, har_file)

    server.stop()  # Stop the proxy server
