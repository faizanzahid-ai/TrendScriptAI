#!/bin/bash
streamlit run app.py --server.address=0.0.0.0 --server.port=8501 &
python grpc_server.py
