# Piggy Bot API

### How to run
#### Dependencies and environment
```bash
$ python3 -m venv .env # Creates virtual python environment
$ source .env/bin/activate # Enter into the virtual environment
$ pip3 install -r requirements.txt # Install dependencies
$ apistar create_tables # Create necessaries tables in database
```
#### Start Server 
```bash
$ DIALOG_FLOW_ACCESS_TOKEN=<token_here> apistar run
```

### Endpoints

URL | Action
------------ | -------------
/query?message= | Parses the given message, delegates to DialogFlow which returns the right intent.
/expenses | List all saved expenses 
/docs | Shows the browseable API Documentation

### PiggyBot DialogFlow Intents

Intent | Description | Example of Input
------------ | ------------- | ---------
register_expense | It represents the intention of registering some expense. | /query?message=Gastei 30 reais
