# Data Science Flask Application Guide


#### Environment Variables

The following environment variables are expected for connection to Postgres server

- URL
- PORT
- USER
- PASS
- DBNAME

#### Running Docker
Build the container

`docker build --tag mentor-app .`

Run the container

`docker run -p 5000:5000 --env-file ./.env mentor-app`

`-p` maps a port inside the container to your local machine.

`--env-file` passes your environment variables to the docker container.

- When you want to quit the app locally, use `Ctrl+C` in the command line to quit.

#### Running App on AWS EB

See more about the EBCLI [here](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-cmd-commands.html?icmpid=docs_elasticbeanstalk_console).

Please note, in all of the below **mentor-app** is a stand in for the name of your application. This name can be changed as necessary.

Initialize the EB docker environment. This only needs to be performed for the first deploy.

`eb init -p docker mentor-app`

- This creates an EB application

Test the application locally

`eb local run --port 5000`

- If all works well, deploy to EB.

Create app on EB. This only needs to be performed for the first deploy.

`eb create mentor-app`

- This will take a while to copy over all files. It will give relevant status updates.

If the application has already been created, to deploy a new version

`eb deploy`

Open the app

`eb open`

- Run this to open the URL in your web browser.

To terminate the application when it is not in use

`eb terminate mentor-app`
