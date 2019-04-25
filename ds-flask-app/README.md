TO-DO

#### Running Docker
Build the container

`docker build --tag flask-app .`

Run the container

`docker run -p 5000:5000`

`-p` maps a port inside the container to your local machine.

#### Running App on AWS EB

Initialize the EB docker environment

`eb init -p docker flask-app`

- This creates an EB application

Test the application locally

`eb local run --port 5000`

- If all works well, deploy to EB.

Create app on EB

`eb create flask-app`

- This will take a while to copy over all files. It will give relevant status updates.

Open the app

`eb open`

- Run this to open the URL in your web browser.
