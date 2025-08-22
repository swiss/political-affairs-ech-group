const express = require('express');
const session = require('express-session');
const axios = require('axios');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Session configuration
app.use(session({
  secret: process.env.SESSION_SECRET || 'fallback-secret-key',
  resave: false,
  saveUninitialized: false,
  cookie: { secure: false } // Set to true in production with HTTPS
}));

// Middleware
app.use(express.static('public'));
app.use(express.json());

// Basic HTML template helper
const htmlTemplate = (title, content) => `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} - eCH GitHub OAuth</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container { 
            background: white; 
            padding: 30px; 
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header { 
            border-bottom: 2px solid #0366d6; 
            padding-bottom: 20px; 
            margin-bottom: 30px;
        }
        .btn { 
            display: inline-block;
            padding: 12px 24px; 
            background: #0366d6; 
            color: white; 
            text-decoration: none; 
            border-radius: 6px;
            font-weight: bold;
            transition: background-color 0.2s;
        }
        .btn:hover { 
            background: #0256cc; 
        }
        .btn-logout { 
            background: #d73a49; 
        }
        .btn-logout:hover { 
            background: #b31d28; 
        }
        .user-info { 
            background: #f6f8fa; 
            padding: 20px; 
            border-radius: 6px;
            margin: 20px 0;
        }
        .avatar { 
            border-radius: 50%; 
            margin-right: 15px;
            vertical-align: middle;
        }
        .error { 
            color: #d73a49; 
            background: #ffeef0; 
            padding: 15px; 
            border-radius: 6px;
            border: 1px solid #fdc1c5;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>eCH Political Affairs - GitHub OAuth Demo</h1>
            <p>This application demonstrates GitHub OAuth integration for the eCH Political Affairs Group.</p>
        </div>
        ${content}
    </div>
</body>
</html>`;

// Routes
app.get('/', (req, res) => {
  if (req.session.user) {
    const content = `
      <h2>Welcome back, ${req.session.user.name || req.session.user.login}!</h2>
      <div class="user-info">
        <img src="${req.session.user.avatar_url}" alt="Avatar" width="60" height="60" class="avatar">
        <strong>GitHub User:</strong> ${req.session.user.login}<br>
        <strong>Name:</strong> ${req.session.user.name || 'Not provided'}<br>
        <strong>Email:</strong> ${req.session.user.email || 'Not provided'}<br>
        <strong>Public Repos:</strong> ${req.session.user.public_repos}<br>
        <strong>Followers:</strong> ${req.session.user.followers}<br>
        <strong>Following:</strong> ${req.session.user.following}
      </div>
      <p>
        <a href="/profile" class="btn">View Full Profile</a>
        <a href="/logout" class="btn btn-logout">Logout</a>
      </p>
    `;
    res.send(htmlTemplate('Dashboard', content));
  } else {
    const content = `
      <h2>GitHub OAuth Login Demo</h2>
      <p>Click the button below to authenticate with your GitHub account.</p>
      <p><a href="/auth/github" class="btn">Login with GitHub</a></p>
      <div style="margin-top: 30px;">
        <h3>About this Demo</h3>
        <p>This application demonstrates:</p>
        <ul>
          <li>GitHub OAuth 2.0 authentication flow</li>
          <li>Retrieving user profile information</li>
          <li>Session management</li>
          <li>Secure token handling</li>
        </ul>
      </div>
    `;
    res.send(htmlTemplate('Login', content));
  }
});

// Initiate GitHub OAuth
app.get('/auth/github', (req, res) => {
  const clientId = process.env.GITHUB_CLIENT_ID;
  const redirectUri = process.env.REDIRECT_URI;
  const scope = 'user:email';
  
  if (!clientId) {
    const content = `
      <div class="error">
        <h2>Configuration Error</h2>
        <p>GitHub Client ID is not configured. Please set up your environment variables.</p>
        <p><a href="/">&larr; Back to Home</a></p>
      </div>
    `;
    return res.send(htmlTemplate('Error', content));
  }

  const authUrl = `${process.env.GITHUB_AUTHORIZE_URL}?client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scope}`;
  res.redirect(authUrl);
});

// GitHub OAuth callback
app.get('/auth/github/callback', async (req, res) => {
  const { code } = req.query;
  
  if (!code) {
    const content = `
      <div class="error">
        <h2>Authorization Error</h2>
        <p>No authorization code received from GitHub.</p>
        <p><a href="/">&larr; Back to Home</a></p>
      </div>
    `;
    return res.send(htmlTemplate('Error', content));
  }

  try {
    // Exchange code for access token
    const tokenResponse = await axios.post(process.env.GITHUB_TOKEN_URL, {
      client_id: process.env.GITHUB_CLIENT_ID,
      client_secret: process.env.GITHUB_CLIENT_SECRET,
      code: code,
    }, {
      headers: {
        Accept: 'application/json',
      },
    });

    const accessToken = tokenResponse.data.access_token;

    if (!accessToken) {
      throw new Error('No access token received');
    }

    // Get user information
    const userResponse = await axios.get(`${process.env.GITHUB_API_URL}/user`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    // Store user info in session
    req.session.user = userResponse.data;
    req.session.accessToken = accessToken;

    res.redirect('/');
  } catch (error) {
    console.error('OAuth callback error:', error);
    const content = `
      <div class="error">
        <h2>Authentication Error</h2>
        <p>Failed to authenticate with GitHub: ${error.message}</p>
        <p><a href="/">&larr; Back to Home</a></p>
      </div>
    `;
    res.send(htmlTemplate('Error', content));
  }
});

// User profile page
app.get('/profile', (req, res) => {
  if (!req.session.user) {
    return res.redirect('/');
  }

  const user = req.session.user;
  const content = `
    <h2>GitHub Profile Details</h2>
    <div class="user-info">
      <img src="${user.avatar_url}" alt="Avatar" width="100" height="100" class="avatar">
      <pre>${JSON.stringify(user, null, 2)}</pre>
    </div>
    <p>
      <a href="/" class="btn">&larr; Back to Dashboard</a>
      <a href="/logout" class="btn btn-logout">Logout</a>
    </p>
  `;
  res.send(htmlTemplate('Profile', content));
});

// Logout
app.get('/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      console.error('Session destroy error:', err);
    }
    res.redirect('/');
  });
});

// API endpoint to get current user (for external applications)
app.get('/api/user', (req, res) => {
  if (!req.session.user) {
    return res.status(401).json({ error: 'Not authenticated' });
  }
  
  res.json({
    user: req.session.user,
    authenticated: true
  });
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ 
    status: 'healthy', 
    timestamp: new Date().toISOString(),
    oauth_configured: !!(process.env.GITHUB_CLIENT_ID && process.env.GITHUB_CLIENT_SECRET)
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log('GitHub OAuth Configuration:');
  console.log(`- Client ID: ${process.env.GITHUB_CLIENT_ID ? 'Configured' : 'Missing'}`);
  console.log(`- Client Secret: ${process.env.GITHUB_CLIENT_SECRET ? 'Configured' : 'Missing'}`);
  console.log(`- Redirect URI: ${process.env.REDIRECT_URI}`);
});

module.exports = app;