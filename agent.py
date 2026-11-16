import os
import asyncio
import websockets
from dotenv import load_dotenv

# Load environment variables from .env file[cite: 3]
load_dotenv()
GNANI_API_KEY = os.getenv("GNANI_API_KEY")

# Gnani API WebSocket endpoint structure (update with official docs endpoint if provided)
GNANI_WS_URL = f"wss://api.gnani.ai/v1/streaming?api_key={GNANI_API_KEY}"

async def run_asha_agent():
    if not GNANI_API_KEY or GNANI_API_KEY == "your_actual_gnani_api_key_here":
        print("Error: Please set your valid GNANI_API_KEY in the .env file.")
        return

    print("Connecting to Gnani API Platform using Prisma v3.0 (STT) and Timbre v3.0 (TTS)...")
    
    try:
        async with websockets.connect(GNANI_WS_URL) as websocket:
            print("Connected successfully via WebSocket!")
            
            # 1. AI Disclosure (Mandatory rule: Agent says it is an AI in its first turn)[cite: 3]
            intro_message = "Namaste. I am your AI assistant for ASHA visit logs. How can I help you record your home visit today?"
            print(f"[Agent]: {intro_message}")
            
            # Keep connection alive for streaming audio and handling responses
            while True:
                # In a full implementation, you send microphone PCM audio chunks here 
                # and receive transcribed text, LLM responses, and synthesized audio back.
                await asyncio.sleep(1)
                
    except Exception as e:
        print(f"WebSocket connection error: {e}")

if __name__ == "__main__":
    asyncio.run(run_asha_agent())