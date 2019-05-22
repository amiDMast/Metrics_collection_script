FROM python:2
RUN pip install psutil
ADD ex.py .
RUN chmod 755 ex.py
RUN chmod +x ex.py 
