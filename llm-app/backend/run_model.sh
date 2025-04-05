#!/bin/bash

# Roda a API com Uvicorn
uvicorn server:app --host 0.0.0.0 --port 5000
