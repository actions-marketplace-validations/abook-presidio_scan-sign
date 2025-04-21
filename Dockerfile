FROM public.ecr.aws/lts/ubuntu:24.04_stable

RUN apt update
RUN apt install -y amazon-ecr-credential-helper curl
COPY aws-signer-notation-cli_amd64.deb  /aws-signer.deb
RUN ls
RUN apt install -y /aws-signer.deb 

RUN curl -o wizcli https://downloads.wiz.io/latest/wizcli-linux-amd64 && chmod +x wizcli

