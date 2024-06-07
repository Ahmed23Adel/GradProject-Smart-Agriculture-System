# Stage 1: Build the Vue.js app
FROM node:16 as build-stage

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Vue.js app
RUN npm run build

# Stage 2: Serve the built app using Nginx
FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

# Create a new directory to copy the built app
RUN mkdir -p /usr/share/nginx/html

# Copy the built app from the build stage to the new directory
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Command to run the app
CMD ["nginx", "-g", "daemon off;"]
