FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy application files
COPY . .

# Default command (overridden in Docker Compose)
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]


