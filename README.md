# {%PROJECT_NAME%}

## Install

```bash

# Install Python service libraries
$ python3 -m venv env \
    && source env/bin/activate \
    && pip install -r requirements.txt \
    && pip install -e .

# Install and build JavaScript libraries
$ npm install \
    && npm run build
```

## Server
```bash

(env) $ python3 -m bin.server [--config config/config.json]
```