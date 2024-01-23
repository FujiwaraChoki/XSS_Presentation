# Script to run frontend and backend Python scripts simultaneously

# Run frontend script in background
( cd frontend && python -m http.server 8080 ) &

# Run backend script
( cd backend && python main.py )
