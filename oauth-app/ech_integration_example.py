"""
Example integration of GitHub OAuth with eCH Political Affairs data processing.

This script demonstrates how to use the GitHub OAuth token to access 
GitHub APIs and integrate with eCH political data schemas.
"""

import os
import requests
import json
from typing import Optional, Dict, Any

class ECHGitHubIntegration:
    """
    Integration class for eCH Political Affairs with GitHub OAuth.
    
    This class provides methods to authenticate users and access
    GitHub data that can be integrated with eCH political schemas.
    """
    
    def __init__(self, oauth_app_url: str = "http://localhost:3000"):
        self.oauth_app_url = oauth_app_url
        self.github_api_base = "https://api.github.com"
    
    def get_authenticated_user(self, session_cookie: str) -> Optional[Dict[str, Any]]:
        """
        Get the authenticated user from the OAuth app.
        
        Args:
            session_cookie: Session cookie from the OAuth app
            
        Returns:
            User data if authenticated, None otherwise
        """
        try:
            response = requests.get(
                f"{self.oauth_app_url}/api/user",
                cookies={"connect.sid": session_cookie}
            )
            
            if response.status_code == 200:
                return response.json()
            return None
            
        except requests.RequestException as e:
            print(f"Error fetching user data: {e}")
            return None
    
    def get_user_repositories(self, access_token: str) -> list:
        """
        Get repositories for the authenticated user.
        
        Args:
            access_token: GitHub access token
            
        Returns:
            List of user repositories
        """
        headers = {"Authorization": f"Bearer {access_token}"}
        
        try:
            response = requests.get(
                f"{self.github_api_base}/user/repos",
                headers=headers
            )
            
            if response.status_code == 200:
                return response.json()
            return []
            
        except requests.RequestException as e:
            print(f"Error fetching repositories: {e}")
            return []
    
    def create_ech_actor_from_github_user(self, github_user: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert GitHub user data to eCH-0294 Actor schema format.
        
        Args:
            github_user: GitHub user data from OAuth
            
        Returns:
            eCH Actor schema compatible dictionary
        """
        return {
            "id": f"github-{github_user.get('id')}",
            "name": [
                {
                    "language": "en",
                    "value": github_user.get("name") or github_user.get("login")
                }
            ],
            "external_ids": [
                {
                    "type": "github",
                    "value": github_user.get("login")
                }
            ],
            "contact_info": {
                "email": github_user.get("email"),
                "website": github_user.get("blog"),
                "github_profile": github_user.get("html_url")
            },
            "metadata": {
                "github_id": github_user.get("id"),
                "created_at": github_user.get("created_at"),
                "public_repos": github_user.get("public_repos"),
                "followers": github_user.get("followers"),
                "following": github_user.get("following")
            }
        }
    
    def create_ech_session_from_github_data(self, repo_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create an eCH-0293 Session from GitHub repository data.
        
        This is an example of how GitHub project data could be mapped
        to eCH political session schemas.
        
        Args:
            repo_data: GitHub repository data
            
        Returns:
            eCH Session schema compatible dictionary
        """
        return {
            "id": f"github-session-{repo_data.get('id')}",
            "name": [
                {
                    "language": "en",
                    "value": repo_data.get("name")
                }
            ],
            "description": repo_data.get("description"),
            "begin_date": repo_data.get("created_at"),
            "url": [
                {
                    "language": "en",
                    "value": repo_data.get("html_url")
                }
            ],
            "metadata": {
                "github_repo_id": repo_data.get("id"),
                "language": repo_data.get("language"),
                "stars": repo_data.get("stargazers_count"),
                "forks": repo_data.get("forks_count")
            }
        }

def example_usage():
    """
    Example usage of the eCH GitHub integration.
    """
    integration = ECHGitHubIntegration()
    
    # Example: Get user data (requires session cookie from browser)
    # In a real application, this would be handled by your web framework
    session_cookie = "your_session_cookie_here"
    
    user_data = integration.get_authenticated_user(session_cookie)
    
    if user_data and user_data.get("authenticated"):
        github_user = user_data["user"]
        
        # Convert to eCH Actor format
        ech_actor = integration.create_ech_actor_from_github_user(github_user)
        
        print("eCH Actor Schema:")
        print(json.dumps(ech_actor, indent=2))
        
        # Get user repositories (requires access token)
        # Note: You would need to store the access token securely
        # This is just an example of the data structure
        
        example_repo = {
            "id": 123456,
            "name": "political-data-project",
            "description": "A project for managing political data",
            "created_at": "2023-01-01T00:00:00Z",
            "html_url": "https://github.com/user/political-data-project",
            "language": "Python",
            "stargazers_count": 42,
            "forks_count": 7
        }
        
        # Convert to eCH Session format (as an example)
        ech_session = integration.create_ech_session_from_github_data(example_repo)
        
        print("\neCH Session Schema:")
        print(json.dumps(ech_session, indent=2))

if __name__ == "__main__":
    example_usage()