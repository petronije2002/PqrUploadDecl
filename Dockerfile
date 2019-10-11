# Use an official Python runtime as a parent image
FROM python:3.6


# Set the working directory to /app
WORKDIR /

# Copy the current directory contents into the container at /app
ADD . /

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y gcc unixodbc-dev

RUN pip install  -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV CONN_STRING=Driver="{ODBC Driver 17 for SQL Server};Server=tcp:resource1.database.windows.net,1433;Database=PqrUploadDeclarations;Uid=pqruploadapp@resource1;PWD=pqruploadazure1!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
ENV FLASK_APP="startup:app"
# Run app.py when the container launches
CMD ["flask run"]
