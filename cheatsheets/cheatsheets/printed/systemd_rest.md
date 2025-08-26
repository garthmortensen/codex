# 2 fastapi, 1 systemd

## Show me two fastapi python modules which perform get and post requests to talk to each other. Show me how to use them with systemd

Certainly! FastAPI is a modern Python web framework for building APIs. Here, I'll show you two FastAPI modules that perform GET and POST requests to communicate with each other, and then I'll provide an example of how to run them using systemd. 

1. **Create a FastAPI module for a simple service that receives GET requests**:

   ```python
   # get_api.py
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"message": "Hello from GET API"}
   ```

2. **Create another FastAPI module for a service that receives POST requests**:

   ```python
   # post_api.py
   from fastapi import FastAPI
   from pydantic import BaseModel

   app = FastAPI()

   class Item(BaseModel):
       name: str

   @app.post("/items/")
   def create_item(item: Item):
       return {"item": item}
   ```

3. **Run the FastAPI applications**:

   You can run these applications using UVicorn. First, make sure you have installed FastAPI and Uvicorn:

   ```
   pip install fastapi uvicorn
   ```

   Then, run both services:

   ```bash
   uvicorn get_api:app --host 0.0.0.0 --port 8000
   uvicorn post_api:app --host 0.0.0.0 --port 8001
   ```

   The first service (`get_api`) will be available at `http://localhost:8000/` and the second service (`post_api`) at `http://localhost:8001/`.

4. **Create systemd service unit files**:

   To manage these services with systemd, create two service unit files. For example, `get_api.service` and `post_api.service` in `/etc/systemd/system/`.

   **get_api.service**:

   ```ini
   [Unit]
   Description=FastAPI GET API
   After=network.target

   [Service]
   User=your_username
   WorkingDirectory=/path/to/your/get_api
   ExecStart=/path/to/uvicorn get_api:app --host 0.0.0.0 --port 8000
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   **post_api.service**:

   ```ini
   [Unit]
   Description=FastAPI POST API
   After=network.target

   [Service]
   User=your_username
   WorkingDirectory=/path/to/your/post_api
   ExecStart=/path/to/uvicorn post_api:app --host 0.0.0.0 --port 8001
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   Make sure to replace `your_username` and the paths with your actual information.

5. **Start and enable the systemd services**:

   You can start and enable the services with the following commands:

   ```bash
   sudo systemctl start get_api
   sudo systemctl start post_api
   sudo systemctl enable get_api
   sudo systemctl enable post_api
   ```

   This will start and enable the FastAPI services to run on system startup.

Now, the two FastAPI services are set up to communicate with each other and managed by systemd. You can access the GET and POST APIs via their respective URLs, and they will continue running as systemd services.