FROM alpine:latest as builder

WORKDIR /home/app

COPY . .

RUN apk add gcc libc-dev; \
    gcc -o main main.c 

COPY --from=builder /home/app/main .

USER 1000
