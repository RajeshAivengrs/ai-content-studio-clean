#!/usr/bin/env python3
"""
AI Content Studio - Minimal Version with Interactive UI
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
                    .test-btn {
                        background: linear-gradient(45deg, #ff6b6b, #ee5a24);
                        color: white;
                        border: none;
                        padding: 12px 24px;
                        border-radius: 25px;
                        cursor: pointer;
                        margin: 10px;
                        font-size: 1rem;
                        text-decoration: none;
                        display: inline-block;
                    }
                    .test-btn:hover {
                        transform: translateY(-2px);
                        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
                    }
                    .result {
                        margin-top: 20px;
                        padding: 15px;
                        background: rgba(0,0,0,0.3);
                        border-radius: 10px;
                        font-family: monospace;
                        white-space: pre-wrap;
                        text-align: left;
                        max-height: 300px;
                        overflow-y: auto;
                    }
                    .api-section {
                        background: rgba(255,255,255,0.1);
                        padding: 30px;
                        border-radius: 15px;
                        margin: 40px 0;
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
                    
                    <div class="api-section">
                        <h2>🧪 Test API Endpoints</h2>
                        <button class="test-btn" onclick="testHealth()">Health Check</button>
                        <button class="test-btn" onclick="testAPI()">API Test</button>
                        <button class="test-btn" onclick="testScriptGeneration()">Generate Script</button>
                        <div class="result" id="result">Click a button above to test the API endpoints...</div>
                    </div>
                </div>

                <script>
                    async function testHealth() {
                        showResult('Testing health endpoint...');
                        try {
                            const response = await fetch('/health');
                            const data = await response.json();
                            showResult(JSON.stringify(data, null, 2));
                        } catch (error) {
                            showResult('Error: ' + error.message);
                        }
                    }
                    
                    async function testAPI() {
                        showResult('Testing API endpoint...');
                        try {
                            const response = await fetch('/api/test');
                            const data = await response.json();
                            showResult(JSON.stringify(data, null, 2));
                        } catch (error) {
                            showResult('Error: ' + error.message);
                        }
                    }
                    
                    async function testScriptGeneration() {
                        showResult('Testing script generation...');
                        try {
                            const response = await fetch('/api/scripts/generate?topic=AI%20and%20Technology');
                            const data = await response.json();
                            showResult(JSON.stringify(data, null, 2));
                        } catch (error) {
                            showResult('Error: ' + error.message);
                        }
                    }
                    
                    function showResult(text) {
                        document.getElementById('result').textContent = text;
                    }
                    
                    // Auto-test health on load
                    window.onload = function() {
                        testHealth();
                    };
                </script>
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
                "platform": "python-http-server",
                "uptime": "running",
                "features": ["health_check", "api_test", "script_generation"]
            }
            self.wfile.write(json.dumps(response, indent=2).encode())
            
        elif self.path == '/api/test':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "message": "API is working perfectly!",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "success": True,
                "service": "ai-content-studio",
                "endpoints": {
                    "health": "/health",
                    "api_test": "/api/test",
                    "script_generation": "/api/scripts/generate?topic=YourTopic"
                }
            }
            self.wfile.write(json.dumps(response, indent=2).encode())
            
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
4. **Impact**: Transforming how we work and live

## Key Benefits
- Increased productivity and efficiency
- Enhanced decision-making capabilities
- Streamlined workflows and processes
- Competitive advantage in the market

## Call to Action
Ready to explore {topic} further? Let's connect and discuss how this can benefit your organization.

---
*Generated by AI Content Studio v1.0*
*Timestamp: {datetime.now(timezone.utc).isoformat()}*
*Word Count: {len(topic.split()) + 50} words*
            """.strip()
            
            response = {
                "success": True,
                "script": script,
                "topic": topic,
                "word_count": len(script.split()),
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "service": "ai-content-studio"
            }
            self.wfile.write(json.dumps(response, indent=2).encode())
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {"error": "Not found", "available_endpoints": ["/", "/health", "/api/test", "/api/scripts/generate"]}
            self.wfile.write(json.dumps(response, indent=2).encode())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    with socketserver.TCPServer(("", port), AIContentStudioHandler) as httpd:
        print(f"Server running on port {port}")
        httpd.serve_forever()