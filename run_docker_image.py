import subprocess
import asyncio
from uvicorn import Config, Server

def run_docker_image():
    try:
        subprocess.run(["docker", "run", "-p", "8000:8000", "walmart-scrapi"], check=True)
        print("Docker image is running on port 8000.")
    except subprocess.CalledProcessError:
        print("Failed to run Docker image.")

if __name__ == "__main__":
    try:
        run_docker_image()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Stopping Docker container gracefully.")
        loop = asyncio.get_event_loop()
        server = Server(Config("app:app", host="0.0.0.0", port=8000))
        loop.run_until_complete(server.serve())
        loop.close()
