# Experiments with Azure Functions and WSGI

This sample mounts various WSGI compliant web frameworks into a single [Azure Function](https://docs.microsoft.com/azure/azure-functions/functions-reference-python?WT.mc_id=academic-0000-cephilli) app using the [azf-wsgi](https://github.com/vtbassmatt/azf-wsgi) package.

| Framework | Matched Routes   |
| --------- | ---------------- |
| Raw WSGI  | wsgi/{\*route}   |
| Bottle    | bottle/{\*route} |
| Flask     | flask/{\*route}  |

## Installing

If you have use [poetry](https://poetry.eustace.io) to manage your Python project dependencies, you can use the following command

```bash
> poetry install
```

This will create the virtual environment and install the required packages.

Otherwise, you can install via pip

```bash
> python -m venv .venv
> source .venv/bin/activate
> python -m pip install -r requirements.txt
```

## Running locally

```bash
> func host start
```

You should see the following routes written to the output:

```
HTTP Functions:

        WsgiApi: [GET,POST,PUT,DELETE,PATCH] http://localhost:7071/wsgi/{*route}

        BottleTrigger: [GET,POST,PUT,DELETE,PATCH] http://localhost:7071/bottle/{*route}

        FlaskTrigger: [GET,POST,PUT,DELETE,PATCH] http://localhost:7071/flask/{*route}
```
