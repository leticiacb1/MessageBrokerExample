### 📬️ Message Broker (RabbitMQ)

#### Run the project

Create a `venv` and install dependencies:

```bash
    # Create environment
    python3 -m venv venv  

    # Activate environment
    source venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt
``` 

Create a `.env` file inside `config/` folder with user and password of RabbitMQ:

```bash
    # .env content'
    RABBIT_USERNAME = 'user'
    RABBIT_PASSWORD = 'password'
``` 

This values has to be the same as the `config/docker-compose.yml` file.

```yml
    # .yaml content

    services:
        rabbitmq:
            image: rabbitmq:3-management
            container_name: rabbitmq
            restart: always
            ports:
            - 5672:5672
            - 15672:15672
            volumes:
            - ./rabbitmq:/var/lib/rabbitmq
            environment:
            - RABBITMQ_DEFAULT_USER=same_as_env
            - RABBITMQ_DEFAULT_PASS=same_as_env
```

For start **RabbitMAQ**:

```bash
    cd config/
    docker compose build
    docker compose up
``` 

Then, go to http://localhost:15672/ to access the RabbitMQ Web admin and log with password and username used in `.yml` file.

In one terminal run teh producer and in the other terminal run the consumer.

```bash
    # Terminal 1
    python3 producer.py
``` 

```bash
    # Terminal 2
    python3 consumer.py
``` 

Create others consumers and see how they interact with the producer. 


<br>
@2024, Insper. 9° Semester,  Computer Engineering.
<br>

_Machine Learning Ops & Interviews Discipline_
