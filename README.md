# Simple HTTP Server

A basic HTTP server implementation in Python that serves static HTML content.

## Features

- Simple HTTP server listening on port 8080
- Handles basic GET requests
- Serves static index.html file
- Basic error handling for malformed requests and missing files
- Socket reuse enabled for development convenience

## Requirements

- Python 3.x11
- No external dependencies required

## Setup

1. Make sure you have Python installed on your system
2. Create an `index.html` file in the same directory as the server script
3. Run the server:
   ```bash
   python main.py
   ```

## Usage

1. Start the server
2. The server will listen on `0.0.0.0:8080`
3. Access the server through a web browser at `http://localhost:8080`

## File Structure

```
├── main.py        # Main server implementation
└── index.html     # Static HTML file to serve
```

## Error Handling

The server includes basic error handling for:
- Malformed HTTP requests
- Missing index.html file
- General file reading errors

## Technical Details

- Server Host: 0.0.0.0 (accessible from any network interface)
- Port: 8080
- Connection backlog: 5 connections
- Maximum request size: 1500 bytes
