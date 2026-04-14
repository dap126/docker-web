FROM python:3.10-alpine
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chown -R appuser:appgroup /usr/src/app
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
