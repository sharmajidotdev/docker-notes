# Stage 1: Build dependencies
FROM node:20-alpine AS builder

# Set metadata labels
LABEL maintainer="Your Name <your.email@example.com>"
LABEL description="A secure and optimized Dockerized Node.js app"

# Set build arguments
ARG NODE_ENV=production
ENV NODE_ENV=$NODE_ENV

# update npm
RUN npm install -g npm

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm i
RUN npm ci --only=$NODE_ENV

# Copy application files
COPY . .

# Stage 2: Create a minimal runtime image
FROM node:20-alpine 

#update npm
RUN npm install -g npm

# Security: Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Set environment variables
ENV PORT=4000
EXPOSE 4000

# Copy only necessary files from builder stage
WORKDIR /app
COPY --from=builder /app /app

# Run the application
ENTRYPOINT ["node", "server.js"]

