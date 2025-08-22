# GitHub OAuth Application

This is a simple Node.js web application that demonstrates GitHub OAuth integration for the eCH Political Affairs Group.

## Features

- GitHub OAuth 2.0 authentication
- User profile display
- Session management
- RESTful API endpoint for user data
- Health check endpoint
- Responsive web interface

## Setup Instructions

### 1. Create a GitHub OAuth App

1. Go to GitHub Settings → Developer settings → OAuth Apps
2. Click "New OAuth App"
3. Fill in the application details:
   - **Application name**: eCH Political Affairs OAuth Demo
   - **Homepage URL**: `http://localhost:3000`
   - **Authorization callback URL**: `http://localhost:3000/auth/github/callback`
4. Save the **Client ID** and **Client Secret**

### 2. Environment Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and fill in your GitHub OAuth credentials:
   ```bash
   GITHUB_CLIENT_ID=your_actual_client_id
   GITHUB_CLIENT_SECRET=your_actual_client_secret
   SESSION_SECRET=generate_a_random_string_here
   ```

### 3. Install Dependencies

```bash
npm install
```

### 4. Run the Application

Development mode (with auto-reload):
```bash
npm run dev
```

Production mode:
```bash
npm start
```

The application will be available at `http://localhost:3000`

## API Endpoints

### Web Interface
- `GET /` - Home page (login or dashboard)
- `GET /auth/github` - Initiate GitHub OAuth
- `GET /auth/github/callback` - OAuth callback handler
- `GET /profile` - User profile page
- `GET /logout` - Logout and destroy session

### API Endpoints
- `GET /api/user` - Get current authenticated user data (JSON)
- `GET /health` - Health check and configuration status

## Usage Examples

### Web Interface
1. Visit `http://localhost:3000`
2. Click "Login with GitHub"
3. Authorize the application on GitHub
4. View your profile information

### API Usage
```bash
# Check if user is authenticated
curl http://localhost:3000/api/user

# Health check
curl http://localhost:3000/health
```

## Security Considerations

- Never commit your `.env` file to version control
- Use HTTPS in production
- Set `cookie.secure = true` in production
- Generate a strong random session secret
- Regularly rotate your GitHub OAuth credentials

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GITHUB_CLIENT_ID` | GitHub OAuth App Client ID | Yes |
| `GITHUB_CLIENT_SECRET` | GitHub OAuth App Client Secret | Yes |
| `SESSION_SECRET` | Secret key for session encryption | Yes |
| `PORT` | Server port (default: 3000) | No |
| `REDIRECT_URI` | OAuth callback URL | No |

## OAuth Flow

1. User clicks "Login with GitHub"
2. App redirects to GitHub OAuth authorization URL
3. User authorizes the application
4. GitHub redirects back to app with authorization code
5. App exchanges code for access token
6. App uses access token to fetch user profile
7. User information is stored in session
8. User is redirected to dashboard

## Error Handling

The application includes comprehensive error handling for:
- Missing environment variables
- OAuth authorization failures
- Network errors during token exchange
- Invalid or expired sessions

## Development

The application is built with:
- **Express.js** - Web framework
- **express-session** - Session management
- **axios** - HTTP client for API calls
- **dotenv** - Environment variable management

## Contributing

This is a demonstration application for the eCH Political Affairs Group. For production use, consider:
- Adding database persistence for user sessions
- Implementing proper logging
- Adding rate limiting
- Using a production session store
- Adding comprehensive tests