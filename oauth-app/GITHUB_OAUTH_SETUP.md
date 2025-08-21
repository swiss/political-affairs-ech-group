# GitHub OAuth App Configuration Guide

This guide walks you through creating a GitHub OAuth App for the eCH Political Affairs OAuth integration.

## Step 1: Access GitHub Developer Settings

1. Log in to GitHub
2. Go to your **Settings** (click your profile picture → Settings)
3. In the left sidebar, click **Developer settings**
4. Click **OAuth Apps**

## Step 2: Create New OAuth App

1. Click **New OAuth App**
2. Fill out the form:

### Application Details

| Field | Value | Description |
|-------|-------|-------------|
| **Application name** | `eCH Political Affairs OAuth Demo` | Name displayed to users during authorization |
| **Homepage URL** | `http://localhost:3000` | Your application's homepage (use your domain in production) |
| **Application description** | `OAuth demo for eCH Political Affairs Group` | Optional description |
| **Authorization callback URL** | `http://localhost:3000/auth/github/callback` | Where GitHub redirects after authorization |

### Production Configuration

For production deployment, update these URLs:

| Field | Development | Production |
|-------|-------------|------------|
| **Homepage URL** | `http://localhost:3000` | `https://yourdomain.com` |
| **Authorization callback URL** | `http://localhost:3000/auth/github/callback` | `https://yourdomain.com/auth/github/callback` |

## Step 3: Save Credentials

After creating the app:

1. Copy the **Client ID** (visible immediately)
2. Click **Generate a new client secret**
3. Copy the **Client Secret** (shown only once - save it immediately!)

## Step 4: Configure Environment Variables

Add these to your `.env` file:

```bash
GITHUB_CLIENT_ID=your_client_id_here
GITHUB_CLIENT_SECRET=your_client_secret_here
SESSION_SECRET=generate_a_random_secure_string
```

## Step 5: Test the Configuration

1. Start your application: `npm start`
2. Visit `http://localhost:3000`
3. Click "Login with GitHub"
4. You should be redirected to GitHub for authorization

## OAuth Scopes

This application requests the following GitHub scopes:

- `user:email` - Access to user's email addresses

### Additional Scopes (Optional)

You can modify the scopes in `server.js` to request additional permissions:

```javascript
const scope = 'user:email read:user repo'; // Example: add repo access
```

Common scopes:
- `read:user` - Read user profile data
- `user:email` - Access user email addresses
- `repo` - Access repositories
- `read:org` - Read organization membership

## Security Considerations

### Development
- Use `http://localhost` for local development
- Client secrets are visible in your environment

### Production
- **Always use HTTPS** in production
- Store secrets securely (environment variables, secret management services)
- Regularly rotate your OAuth credentials
- Use a strong, randomly generated session secret
- Set `cookie.secure = true` in production

### Environment Variables Security
```bash
# Generate a secure session secret
openssl rand -base64 32

# Example secure configuration
SESSION_SECRET=XkJ9mP2vN8qR5sT7wY1uI3oL6nM9cV2bF4gH8jK0pQ==
```

## Troubleshooting

### Common Issues

1. **"Application not configured"**
   - Check that `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` are set
   - Verify the values are correct (no extra spaces or characters)

2. **"Redirect URI mismatch"**
   - Ensure the callback URL in GitHub matches exactly
   - Check for `http` vs `https` and port numbers

3. **"Access denied"**
   - User canceled authorization
   - Check if the OAuth app is suspended or restricted

### Debug Steps

1. Check the health endpoint: `GET /health`
2. Verify environment variables are loaded
3. Check server logs for detailed error messages
4. Test with GitHub's OAuth documentation

## GitHub OAuth Documentation

- [GitHub OAuth Apps](https://docs.github.com/en/developers/apps/building-oauth-apps)
- [Authorizing OAuth Apps](https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps)
- [Scopes for OAuth Apps](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps)