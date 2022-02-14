FROM python:3.8
WORKDIR /project
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY ./requirements.txt ./app.py ./templates/result.html ./templates/web_app.html  ./
RUN mkdir templates
RUN mv result.html web_app.html templates/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -c "from detoxify import Detoxify; print(Detoxify('original').predict('example test'));"
EXPOSE 5000
CMD ["flask", "run"]