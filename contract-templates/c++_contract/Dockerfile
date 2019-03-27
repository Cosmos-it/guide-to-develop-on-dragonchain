FROM alpine:latest as builder

WORKDIR /home/app

COPY . .

RUN apk add g++; \
    g++ -o main main.cpp contract/handler.cpp

FROM alpine:latest

RUN apk add libstdc++;

WORKDIR /home/app

COPY --from=builder /home/app/main .

USER 1000
