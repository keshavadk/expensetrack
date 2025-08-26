# #!/bin/bash
# # Start FastAPI backend
# uvicorn backend.main:app --host 0.0.0.0 --port 8000 &
# # Start Streamlit frontend
# streamlit run frontend/app.py --server.port 10000 --server.address 0.0.0.0
#!/bin/bash
# start.sh

# Run database migrations (create tables if they don't exist)
#!/bin/bash
set -e

# Start FastAPI backend
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit frontend
streamlit run frontend/streamlit_app.py --server.port 8501 --server.address 0.0.0.0
