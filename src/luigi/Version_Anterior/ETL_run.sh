#!/bin/bash

# Corre las tareas del ETLpipeline
 PYTHONPATH='.' luigi --module luigi_mas_completo run_all --local-scheduler --date --bucket