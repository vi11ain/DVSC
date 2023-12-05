# Configuration
Edit programs served by website:
* `dvsc/programs`
    * Place the files for the programs
* `dvsc/config.py`
    * Edit the `PROGRAMS` dictionary
* `dvsc/static/images`
    * Place images for the programs

**Remember to configure one program as locked for the TOCTOU challenge!**

# Setup
1. Start by setting up a virtual environment:
    ```bash
    python -m virtualenv venv
    venv/Scripts/activate
    ```

2. Install requirements
    ```bash
    pip install -r requirements.txt
    ```

3. Run website
    ```bash
    flask --app dvsc run --port 80
    ```

4. Run token service
    ```bash
    python token_gen.py
    ```

# Startup Script
```bash
./start.sh
```