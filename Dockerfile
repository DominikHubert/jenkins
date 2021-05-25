FROM nginx:1.11-alpine

RUN echo 'Imagebau' && apt-get update
COPY index.html /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
