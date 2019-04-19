FROM python
ADD Death_Note /tmp/Death_Note
RUN pip3 install -r /tmp/Death_Note/requirements.txt
WORKDIR /tmp/Death_Note/
CMD ["python3","-u", "Carry_Out_Justice.py"]
