# GitHub OAuth Integration for eCH Political Affairs

This directory contains a complete GitHub OAuth implementation for applications that need to authenticate users with their GitHub accounts.

## 🎯 Purpose

This OAuth implementation provides:
- Secure GitHub user authentication
- User profile information retrieval
- Session management
- RESTful API endpoints for integration
- Ready-to-use web interface

## 🚀 Quick Start

### 1. Setup the OAuth Application

```bash
cd oauth-app
./setup.sh
```

### 2. Configure GitHub OAuth App

1. Visit [GitHub Developer Settings](https://github.com/settings/developers)
2. Create a new OAuth App with:
   - **Homepage URL**: `http://localhost:3000`
   - **Callback URL**: `http://localhost:3000/auth/github/callback`
3. Copy your Client ID and Client Secret

### 3. Configure Environment

Edit `oauth-app/.env`:
```bash
GITHUB_CLIENT_ID=your_client_id_here
GITHUB_CLIENT_SECRET=your_client_secret_here
SESSION_SECRET=your_random_secret_here
```

### 4. Run the Application

```bash
cd oauth-app
npm start
```

Visit `http://localhost:3000` to test the OAuth flow.

## 📁 Directory Structure

```
oauth-app/
├── server.js                    # Main application server
├── package.json                 # Node.js dependencies
├── README.md                    # Detailed documentation
├── GITHUB_OAUTH_SETUP.md       # GitHub OAuth setup guide
├── setup.sh                    # Automated setup script
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
└── .env                        # Your actual environment variables (not in git)
```

## 🔧 Features

### Web Interface
- **Login Page**: Simple GitHub OAuth login
- **Dashboard**: User profile display after authentication
- **Profile Page**: Detailed GitHub user information
- **Logout**: Secure session termination

### API Endpoints
- `GET /api/user` - Current authenticated user data (JSON)
- `GET /health` - Application health and configuration status

### Security Features
- Secure session management
- Environment variable configuration
- CSRF protection through state parameters
- Secure cookie handling

## 🔐 OAuth Flow

1. **Authorization Request**: User clicks "Login with GitHub"
2. **GitHub Authorization**: User authorizes the application
3. **Authorization Code**: GitHub returns authorization code
4. **Token Exchange**: App exchanges code for access token
5. **User Data**: App fetches user profile using access token
6. **Session Creation**: User data stored in secure session

## 🛠️ Integration Examples

### Express.js Application
```javascript
const express = require('express');
const app = express();

// Check if user is authenticated
app.get('/protected', (req, res) => {
  if (!req.session.user) {
    return res.redirect('/auth/github');
  }
  res.json({ user: req.session.user });
});
```

### API Usage
```bash
# Get current user
curl -b cookies.txt http://localhost:3000/api/user

# Health check
curl http://localhost:3000/health
```

## 🔒 Security Considerations

### Development
- Uses HTTP for local development
- Environment variables stored in `.env`
- Session data stored in memory

### Production Recommendations
- **Use HTTPS only**
- Use secure session store (Redis, database)
- Set `cookie.secure = true`
- Implement rate limiting
- Use environment variable management service
- Regular credential rotation

## 📚 Documentation

- [README.md](oauth-app/README.md) - Complete application documentation
- [GITHUB_OAUTH_SETUP.md](oauth-app/GITHUB_OAUTH_SETUP.md) - GitHub OAuth App setup guide
- [GitHub OAuth Documentation](https://docs.github.com/en/developers/apps/building-oauth-apps)

## 🧪 Testing

### Manual Testing
1. Start the application
2. Visit the home page
3. Click "Login with GitHub"
4. Authorize the application
5. Verify user information is displayed

### Health Check
```bash
curl http://localhost:3000/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2023-...",
  "oauth_configured": true
}
```

## 🚀 Deployment

### Environment Variables for Production
```bash
GITHUB_CLIENT_ID=your_production_client_id
GITHUB_CLIENT_SECRET=your_production_client_secret
SESSION_SECRET=your_secure_random_secret
PORT=3000
REDIRECT_URI=https://yourdomain.com/auth/github/callback
```

### Docker Deployment
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY oauth-app/package*.json ./
RUN npm install --production
COPY oauth-app/ .
EXPOSE 3000
CMD ["npm", "start"]
```

## 🤝 Contributing

This OAuth implementation is part of the eCH Political Affairs Group project. For improvements or issues:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is part of the eCH Political Affairs Group and follows the same licensing terms as the main repository.

## 📞 Support

For questions about this OAuth implementation:
- Check the documentation in this directory
- Review GitHub's OAuth documentation
- Open an issue in this repository

---

**Note**: This is a demonstration implementation. For production use, consider additional security measures, monitoring, and compliance requirements specific to your organization.