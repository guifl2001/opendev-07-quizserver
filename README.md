## About the Application

This application is a web-based platform designed to facilitate the student assignment submission and feedback process for a Software Design (SoftDes) course, specifically labeled as "SoftDes 2018.2." It showcases an example page for "Challenge 1," where the critical functionalities include viewing problem statements, submission deadlines, and feedback/results of submitted assignments. The application features a login functionality so that the users only login with the correct password

The application is built using Flask, a lightweight WSGI web application framework in Python. Flask is known for being simple to set up and flexible, making it ideal for small to medium-sized applications. The platform uses SQL for managing its database operations. SQL databases are robust, allowing for complex queries and transactions necessary for managing course data, assignments, user accounts, submission records, feedback, and results.
### Language:
- *Python*

### Libraries:

1. *flask*:
   - Flask
   - request
   - jsonify
   - abort
   - make_response
   - session
   - render_template
2. *flask_httpauth*: Extensão para autenticação HTTP básica.
   - HTTPBasicAuth
3. *datetime*: Módulo para manipulação de datas e horas.
   - datetime
4. *sqlite3*: Módulo para interação com bancos de dados SQLite.
   - sqlite3
5. *json*: Módulo para manipulação de dados JSON.
   - json
6. *hashlib*: Módulo para algoritmos de hash seguros.
   - hashlib

### Running in local server

1. **Requirements:**

Certifique-se de que SQLite3 está instalado no seu sistema.

- **macOS:**    
```
brew install sqlite3
```
- **Linux (Debian-based, ex.: Ubuntu):**

```
sudo apt-get install sqlite3
```
     
- **Linux (Fedora-based):**
```
sudo dnf install sqlite
```
  
- **Windows:**
Baixe o [SQLite3](https://www.sqlite.org/download.html) e adicione o binário ao seu PATH.

2. **Install the dependencies**

```
pip install flask flask-httpauth
```
or 
```
pip install -r requirements.txt
```

2. **Create the database**

```
sqlite3 quiz.db < quiz.sql
```

or 

```
python setup.py
```

3. **Create the users.csv with your credentials.**

Example:
```
admin,admin
```

4. **Add your user.**

```
python adduser.py
```

5. **Start the development server:**

```
python softdes.py
```

Now you can see in the terminal something like this:
![alt text](static/assets/img/image.png)

If you open the url, you should see this screen:

![alt text](static/assets/img/image-1.png)

### Running with Docker

Considering that you already have users.csv created with your credentials:

1. **Install Docker:**

Ensure Docker is installed on your system. Follow the instructions at [Docker Install](https://docs.docker.com/get-docker/) for your operating system.

2. **Clone the repository:**

Clone the repository containing the application code:

```sh
   git clone <repository_url>
   cd <repository_directory>
```

3. **Create the docker image:**

Build the Docker image for the application using the provided Dockerfile. Make sure to be in the root directory of the project where the Dockerfile is located.

```
docker build -t softdes-app .
```

4. **Run the Docker container:**

Start a Docker container from the built image. This will also set up the database and necessary files.

```
docker run -p 8080:8080 softdes-app
```

5. **Access the application:**

Open your web browser and go to http://localhost:8080 to access the application.

## Running with Docker

Using Docker can simplify the setup and deployment process by encapsulating the environment and dependencies. This guide assumes you have Docker installed on your system. If not, you can download and install Docker from [Docker's official site](https://www.docker.com/get-started).

### Steps to Run the Application with Docker

1. **Build the Docker Image**

   Navigate to the directory containing the Dockerfile and execute the following command to build the Docker image. This command builds an image and tags it as `softdes-app`.

    ```bash
    docker build -t softdes-app .
    ```

2. **Run the Docker Container**

   After the image has been successfully built, you can run the container using the following command. This will start the server inside the container, and it will be accessible through the specified port.

    ```bash
    docker run -d -p 8080:8080 softdes-app
    ```

   Here, `-d` runs the container in detached mode (in the background), and `-p 8080:8080` maps port 8080 of the container to port 8080 on your host, allowing you to access the application via `localhost:8080` in your web browser.

3. **Viewing the Application**

   Open your web browser and go to `http://localhost:8080`. You should now see the SoftDes 2018.2 application running.

4. **Stopping the Container**

   If you need to stop the running container, you can find the container ID using:

    ```bash
    docker ps
    ```

   Then stop the container by:

    ```bash
    docker stop [CONTAINER_ID]
    ```

Replace `[CONTAINER_ID]` with the actual ID of your container.

### Additional Docker Commands

- **View Docker Images**

  To see all the Docker images on your system:

    ```bash
    docker images
    ```

- **View Running Containers**

  To check all currently running Docker containers:

    ```bash
    docker ps
    ```
    
- **Remove Docker Images**

  To remove a Docker image:

    ```bash
    docker rmi [IMAGE_ID]
    ```

  Replace `[IMAGE_ID]` with the ID of the image you want to remove. Note that the image must not be used by any running container.