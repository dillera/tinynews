import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify
import requests
import xml.etree.ElementTree as ET
import platform
import socket
import time

app = Flask(__name__)

# Set up logging
# 🍎 [Python Logging Documentation](https://www.google.com/search?q=python+logging)
handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

start_time = time.time()

NEWS_FEED_URL = "https://feeds.npr.org/1001/rss.xml"

@app.route('/news', methods=['GET', 'POST'])
def get_news():
    # Log the incoming request
    app.logger.debug(f"Incoming request method: {request.method}")
    app.logger.debug(f"Headers: {request.headers}")
    app.logger.debug(f"Request data: {request.data}")

    # If expecting POST with JSON, handle that gracefully if GET is allowed
    if request.method == 'POST':
        try:
            client_data = request.get_json(force=True)
            app.logger.debug(f"Parsed JSON: {client_data}")
        except Exception as e:
            app.logger.error(f"Error parsing JSON: {e}")
            return jsonify({"error": "Invalid JSON"}), 400

    # Make the external request
    try:
        resp = requests.get(NEWS_FEED_URL)
        app.logger.debug(f"External GET to {NEWS_FEED_URL} returned status {resp.status_code}")
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error fetching news feed: {e}")
        return jsonify({"error": "Failed to retrieve news feed"}), 500

    # Parse RSS
    try:
        root = ET.fromstring(resp.text)
        channel = root.find('channel')
        items = channel.findall('item') if channel is not None else []
    except ET.ParseError as e:
        app.logger.error(f"Error parsing XML: {e}")
        return jsonify({"error": "Failed to parse XML"}), 500

    news_list = []
    for item in items:
        title = item.find('title').text if item.find('title') is not None else ""
        link = item.find('link').text if item.find('link') is not None else ""
        description = item.find('description').text if item.find('description') is not None else ""
        pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""

        news_list.append({
            "title": title,
            "link": link,
            "description": description,
            "published": pub_date
        })

    app.logger.debug(f"Returning {len(news_list)} news items")
    return jsonify({"news": news_list}), 200

@app.route('/status', methods=['GET'])
def get_status():
    current_time = time.time()
    uptime_seconds = current_time - start_time
    host_name = socket.gethostname()
    python_version = platform.python_version()
    return jsonify({
        "status": "running",
        "hostname": host_name,
        "python_version": python_version,
        "uptime_seconds": uptime_seconds
    }), 200

if __name__ == '__main__':
    # Enable debug for auto-reload and verbose logging
    app.run(host='0.0.0.0', port=5000, debug=True)
    