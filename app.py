# Flask app (server_pc.py)
from flask import Flask, request
import logging
import os
from datetime import datetime

app = Flask(__name__)

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Configure logging with a relative path
log_file_path = os.path.join(script_dir, 'app.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO)

@app.route('/send-text', methods=['POST'])
def receive_text():
    text = request.form['text']
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_ip = request.remote_addr
    logging.info(f"User {user_ip} accessed the application at {timestamp}.")

    # Process the text as needed
    print('Received text:', text)
    
    return 'Text received successfully'

if __name__ == '__main__':
    app.run()


