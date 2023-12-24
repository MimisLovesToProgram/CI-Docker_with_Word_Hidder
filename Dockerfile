FROM python:3.11-slim

WORKDIR /CI_&_Docker_with_Word_Hidder

COPY . .

CMD ["python", "WordHidder.py"]