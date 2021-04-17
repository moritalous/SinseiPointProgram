FROM public.ecr.aws/lambda/python:3.8

ENV PLAYWRIGHT_BROWSERS_PATH=0

RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    rm -rf /var/cache/yum/* && \
    yum clean all

RUN yum install -y chromium-headless && \
    rm -rf /var/cache/yum/* && \
    yum clean all

COPY requirements.txt ./

RUN python3.8 -m pip install -r requirements.txt

RUN playwright install chromium

COPY app.py ./

CMD ["app.lambda_handler"]

# ENV DEBUG=pw:api,pw:browser*
