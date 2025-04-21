FROM public.ecr.aws/lts/ubuntu:24.04_stable

RUN apt update
RUN apt install python3 python3-pip -y
## Install Notation CLI / ECR Helper 
RUN apt install -y amazon-ecr-credential-helper curl
COPY aws-signer-notation-cli_amd64.deb  /aws-signer.deb
RUN apt install -y /aws-signer.deb 

## Install Python Packages 
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages
#RUN apt install -y python3-Flask python3-Jsonify
RUN ls
COPY app.py .

## Install WIZ CLI 
RUN curl -o wizcli https://downloads.wiz.io/latest/wizcli-linux-amd64 && chmod +x wizcli

EXPOSE 6000
CMD ["python3", "app.py"]
