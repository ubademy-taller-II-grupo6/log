FROM python
WORKDIR /app
COPY ./config/*.py ./config/
COPY ./models/*.py ./models/
COPY ./routers/*.py ./routers/
COPY ./schemas/*.py ./schemas/
COPY ./app.py ./
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install pymongo[srv]
ENV PORT=5000
CMD [ "python3", "app.py" ]
