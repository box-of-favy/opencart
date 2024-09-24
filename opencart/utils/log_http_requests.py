def log_http_requests(proxy, logger):
    """
    Logs the HTTP requests and responses captured by the proxy.

    :param proxy: Proxy object used to capture HTTP traffic.
    :param logger: Logger object used to log the HTTP requests and responses.
    """
    try:
        # Getting HAR (HTTP Archive) data from proxy
        har_data = proxy.har

        # We go through all the records that the proxy intercepted
        for entry in har_data['log']['entries']:
            request = entry['request']
            response = entry['response']

            # Logging the request
            logger.info(f"Request: {request['method']} {request['url']}")

            # Logging the response
            logger.info(f"Response: {response['status']} {response['statusText']}")

    except Exception as e:
        logger.error(f"Error while logging HTTP requests: {e}")