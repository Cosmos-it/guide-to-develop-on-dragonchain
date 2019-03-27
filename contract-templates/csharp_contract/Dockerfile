FROM microsoft/dotnet:2.1-sdk as builder

# Supress collection of data.
ENV DOTNET_CLI_TELEMETRY_OPTOUT 1

# Optimize for Docker builder caching by adding projects first.
WORKDIR /home/app/src/
COPY ./*.csproj  .
RUN dotnet restore ./root.csproj

COPY .  .

RUN dotnet publish -c release -o published

FROM microsoft/dotnet:2.1-runtime

WORKDIR /home/app/
COPY --from=builder /home/app/src/published .
RUN chown 1000:1000 -R /home/app

USER 1000

