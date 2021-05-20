FROM nginx:1.11-alpine

RUN echo 'Imagebau'
COPY index.html /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
