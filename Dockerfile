FROM python:3.9.0

COPY . /longest_word_app

WORKDIR /longest_word_app

RUN pip install -r requirements.txt

WORKDIR /longest_word_app/tests

RUN mkdir -p report

ENTRYPOINT ["pytest"]
CMD ["-v", "--html-report=/report/longest_transpose_word_testcases_docker.html"]

