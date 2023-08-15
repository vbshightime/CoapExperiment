import time
import asyncio
import aiocoap

async def main():
    protocol = await aiocoap.Context.create_client_context()

    # Replace 'your-raspberry-pi-ip' with the actual IP address of your Raspberry Pi
    request = aiocoap.Message(code=aiocoap.GET, uri=f"coap://192.168.81.100/coap")
    start_time = time.time()
    try:
        response = await protocol.request(request).response
        end_time = time.time()
        get_latency = end_time - start_time
        print(f"Request Latency: {get_latency:.4f} seconds")
        print("Response:", response.payload.decode())
    except Exception as e:
        print("Failed to fetch resource:", e)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
