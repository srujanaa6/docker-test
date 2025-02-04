FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
# Set the PYTHONPATH to include /app, so Python can find the app module
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Start the application or run tests (you can modify this as needed)
CMD ["python", "app/main.py"]
