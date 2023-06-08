FROM python:3.9

# Set general environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive


# Set enviroment variables for versions of firefox and geckodriver
ENV GECKODRIVER_VER v0.33.0
ENV FIREFOX_VER 102.0
 
RUN set -x \
   && apt update \
   && apt upgrade -y \
   && apt install -y \
       firefox-esr 

# Add latest FireFox
RUN set -x \
   && apt install -y \
       libx11-xcb1 \
       libdbus-glib-1-2 \
   && curl -sSLO https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2 \
   && tar -jxf firefox-* \
   && mv firefox /opt/ \
   && chmod 755 /opt/firefox \
   && chmod 755 /opt/firefox/firefox
  
# Add geckodriver
RUN set -x \
   && curl -sSLO https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz \
   && tar zxf geckodriver-*.tar.gz \
   && mv geckodriver /usr/bin/
 

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .

# Install the requirements.txt and make sure selenium is on latest version
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade selenium

# Copy the FastAPI project code into the container
COPY . .

# Expose the port on which the FastAPI app will run
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
