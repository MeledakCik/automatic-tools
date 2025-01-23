import requests
import re
import json
import base64

class InstagramFollowListAPI:
    BASE_URL = "https://www.instagram.com/api/v1/friendships"

    def __init__(self, cookies):
        self.auth_token = self._extract_auth_token(cookies)
        self.headers = {
            "Authorization": f"Bearer {self.auth_token}",
            "Content-Type": "application/json",
            "User-Agent": "Instagram 123.0.0.26.121"
        }

    def _extract_auth_token(self, cookies):
        try:
            if 'Bearer IGT:2:' in cookies:
                ig_set_auth = re.search(r'"IG-Set-Authorization": "(.*?)"', cookies).group(1)
                decoded_token = json.loads(base64.urlsafe_b64decode(ig_set_auth.split('Bearer IGT:2:')[1]))
                return ";".join([f"{k}={v}" for k, v in decoded_token.items()])
            else:
                raise ValueError("Token tidak ditemukan dalam cookie.")
        except Exception as e:
            print(f"Error extracting token: {e}")
            return None

    def get_mutual_followers(self, user_id, max_id=None, page_size=12):
        url = f"https://www.instagram.com/api/v1/friendships/{user_id}/mutual_followers/"
        params = {"max_id": max_id, "page_size": page_size}
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching mutual followers: {e}")
            return None

    def get_followers(self, user_id, max_id=None, page_size=12):
        url = f"https://www.instagram.com/api/v1/friendships/{user_id}/followers/"
        params = {"max_id": max_id, "count": page_size}
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching followers: {e}")
            return None

    def get_following(self, user_id, max_id=None, page_size=12):
        url = f"https://www.instagram.com/api/v1/friendships/{user_id}/following/"
        params = {"max_id": max_id, "count": page_size}
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching following: {e}")
            return None

    def get_relationship_info(self, target_user_id):
        url = f"https://www.instagram.com/api/v1/friendships/show/{target_user_id}/"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching relationship info: {e}")
            return None

if __name__ == "__main__":
    cookies = 'masukkan_cookie_di_sini'
    user_id = '123456789'
    api = InstagramFollowListAPI(cookies)
    print("Mutual Followers:")
    mutual_followers = api.get_mutual_followers(user_id)
    print(mutual_followers)
    print("\nFollowers:")
    followers = api.get_followers(user_id)
    print(followers)
    print("\nFollowing:")
    following = api.get_following(user_id)
    print(following)
    print("\nRelationship Info:")
    relationship_info = api.get_relationship_info(user_id)
    print(relationship_info)
