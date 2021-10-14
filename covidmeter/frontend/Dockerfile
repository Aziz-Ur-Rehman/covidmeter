FROM node:alpine
WORKDIR /Users/raveedahmad/Gitlab/training-repo/raveed-covidmeter/frontend/docker
COPY package.json /Users/raveedahmad/Gitlab/training-repo/raveed-covidmeter/frontend/docker
COPY package-lock.json /Users/raveedahmad/Gitlab/training-repo/raveed-covidmeter/frontend/docker
COPY ./ /Users/raveedahmad/Gitlab/training-repo/raveed-covidmeter/frontend/docker
RUN npm i
CMD ["npm", "run", "start"]