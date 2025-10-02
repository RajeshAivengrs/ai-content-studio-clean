#!/usr/bin/env python3
"""
AI Content Studio - Minimal Version
Uses only Python standard library - guaranteed to work
"""

import http.server
import socketserver
import json
import os
from datetime import datetime, timezone
from urllib.parse import urlparse, parse_qs

class AIContentStudioHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>AI Content Studio - Live!</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        margin: 0;
                        padding: 20px;
                        color: white;
                        min-height: 100vh;
                    }
                    .container {
                        max-width: 800px;
                        margin: 0 auto;
                        text-align: center;
                    }
                    .header h1 {
                        font-size: 3rem;
                        margin-bottom: 10px;
                    }
                    .status {
                        background: rgba(0,255,0,0.2);
                        padding: 20px;
                        border-radius: 10px;
                        margin: 20px 0;
                    }
                    .feature {
                        background: rgba(255,255,255,0.1);
                        padding: 20px;
                        border-radius: 10px;
                        margin: 20px 0;
                    }
                    a {
                        color: #ffd700;
                        text-decoration: none;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🚀 AI Content Studio</h1>
                        <p>Successfully Deployed on Render!</p>
                    </div>
                    
                    <div class="status">
                        <h3>✅ Service is Live and Healthy!</h3>
                        <p>Minimal version - uses only Python standard library!</p>
                    </div>
                    
                    <div class="feature">
                        <h3>🧪 Test API Endpoints</h3>
                        <p><a href="/health">Health Check</a> | 
                           <a href="/api/test">API Test</a> | 
                           <a href="/api/scripts/generate?topic=AI">Generate Script</a></p>
                    </div>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
            
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "status": "healthy",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "service": "ai-content-studio",
                "version": "1.0.0",
                "environment": "render",
                "platform": "python-http-server"
            }
            self.wfile.write(json.dumps(response).encode())
            
        elif self.path == '/api/test':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "message": "API is working!",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "success": True
            }
            self.wfile.write(json.dumps(response).encode())
            
        elif self.path.startswith('/api/scripts/generate'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            # Parse query parameters
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            topic = query_params.get('topic', ['AI and Technology'])[0]
            
            script = f"""
# {topic} - AI Generated Script

## Introduction
Welcome to this exciting exploration of {topic}. Today we'll dive deep into the fascinating world of {topic.lower()} and discover how it's revolutionizing our industry.

## Main Content
{topic} represents a paradigm shift in how we approach complex problems. The key insights include:

1. **Innovation**: {topic} brings unprecedented opportunities
2. **Efficiency**: Streamlined processes and workflows  
3. **Growth**: Scalable solutions for the future

## Call to Action
Ready to explore {topic} further? Let's connect and discuss how this can benefit your organization.

---
*Generated by AI Content Studio v1.0*
*Timestamp: {datetime.now(timezone.utc).isoformat()}*
            """.strip()
            
            response = {
                "success": True,
                "script": script,
                "topic": topic,
                "word_count": len(script.split()),
                "generated_at": datetime.now(timezone.utc).isoformat()
            }
            self.wfile.write(json.dumps(response).encode())
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {"error": "Not found"}
            self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    with socketserver.TCPServer(("", port), AIContentStudioHandler) as httpd:
        print(f"Server running on port {port}")
        httpd.serve_forever()
