FROM node:8.9.1-alpine

WORKDIR /home/app

# Wrapper/boot-strapper
COPY package.json .

# This ordering means the npm installation is cached for the outer function handler.
RUN NPM_CONFIG_LOGLEVEL=warn npm i --production

# Copy outer function handler
COPY . .

# chmod for tmp is for a buildkit issue (@alexellis)
RUN chown 1000:1000 -R /home/app

USER 1000


