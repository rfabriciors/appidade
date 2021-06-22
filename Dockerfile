FROM nginx
LABEL "vendor"="Taligent"
LABEL version="v1.2n"
LABEL description="Aplicação de cálculo de idade com JavaScript"
LABEL maintainer="rfabriciors@gmail.com"

COPY www/ /usr/share/nginx/html


EXPOSE 80