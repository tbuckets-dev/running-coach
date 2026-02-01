import requests

# 1. Configuration
# Change this to your Cloudflare Tunnel URL or http://localhost:8000
BASE_URL = "http://localhost:8000" 
ENDPOINT = "/webhooks/strava"
VERIFY_TOKEN = "your_super_secret_verify_token" # Must match settings.STRAVA_VERIFY_TOKEN
CHALLENGE_STRING = "sample_challenge_123"

def test_handshake():
    # 2. Construct the URL with query parameters
    # This mimics exactly what Strava's servers do
    params = {
        "hub.mode": "subscribe",
        "hub.verify_token": VERIFY_TOKEN,
        "hub.challenge": CHALLENGE_STRING
    }

    print(f"Testing handshake at: {BASE_URL}{ENDPOINT}")

    # 3. Send the GET request
    response = requests.get(f"{BASE_URL}{ENDPOINT}", params=params)

    # 4. Analyze the result
    if response.status_code == 200:
        data = response.json()
        if data.get("hub.challenge") == CHALLENGE_STRING:
            print("✅ SUCCESS: Handshake verified!")
            print(f"Response from server: {data}")
        else:
            print("❌ FAILURE: Server responded, but challenge didn't match.")
    else:
        print(f"❌ FAILURE: Server returned status code {response.status_code}")
        print(f"Error detail: {response.text}")

if __name__ == "__main__":
    test_handshake()