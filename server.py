from src import main
import os
import uvicorn




#if __name__ == "__main__":
#  uvicorn.run("src.main:app", host=HOST, port=10000, reload=True)
#if __name__ == "__main__":
#  uvicorn.run("src.main:app", port=8000, reload=True)

PORT = int(8001)
#PORT = int(10000)
HOST = '0.0.0.0'

if __name__ == "__main__":
  uvicorn.run("src.main:app", host=HOST, port=PORT, reload=True)
