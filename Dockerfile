# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port available if required
# EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "time_series_eda.py"]


# steps
# docker build -t ml-docker-app .
# docker run ml-docker-app
# docker run -p 5000:5000 my-ml-model	# if using port
