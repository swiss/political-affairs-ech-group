#!/bin/bash

echo "=== eCH Political Affairs - GitHub OAuth App Setup ==="
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js from https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js version: $(node --version)"

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm."
    exit 1
fi

echo "✅ npm version: $(npm --version)"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
npm install

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Dependencies installed successfully"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "✅ .env file created. Please edit it with your GitHub OAuth credentials."
else
    echo "⚠️  .env file already exists. Skipping creation."
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a GitHub OAuth App at: https://github.com/settings/developers"
echo "2. Edit the .env file with your Client ID and Client Secret"
echo "3. Run 'npm start' to start the application"
echo "4. Visit http://localhost:3000 to test the OAuth flow"
echo ""
echo "For more details, see README.md"