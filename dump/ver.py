import requests
import random
import time
from rich.console import Console

console = Console()

# API Endpoint & Headers
IG_API = 'https://i.instagram.com/api/v1/'
HEADERS = {
    'Host': 'www.instagram.com',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'x-asbd-id': '129477',
    'x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E',
    'sec-fetch-site': 'same-origin',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5',
    'cookie': 'ds_user_id=68041199890;sessionid=68041199890%3Ar3hPPtUvs7Czyx%3A27%3AAYceaDLAR0hEU9n65sIDVs3IY9rLTHwgkGGgB7QQmQ'
}


# File to save the results
RESULT_FILE = "usernames_dump.txt"

# Dump usernames based on the target
def dump_usernames(target_username, depth=1, max_depth=3, processed=None):
    if processed is None:
        processed = set()

    if depth > max_depth or target_username in processed:
        return

    try:
        # Get user info
        console.log(f"Fetching info for [bold blue]{target_username}[/]")
        response = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={target_username}", headers=HEADERS)
        user_data = response.json()
        
        if not response.ok or 'data' not in user_data:
            console.log(f"[red]Failed to fetch data for {target_username}[/]")
            return

        user_id = user_data['data']['user']['id']
        followers_endpoint = f"https://i.instagram.com/api/v1/friendships/{user_id}/followers/"

        # Fetch followers
        console.log(f"Fetching followers for [bold green]{target_username}[/]")
        followers_response = requests.get(followers_endpoint, headers=HEADERS)
        followers_data = followers_response.json()

        if 'users' not in followers_data:
            console.log(f"[red]No followers found for {target_username}[/]")
            return

        # Process followers
        followers = [f['username'] for f in followers_data['users']]
        console.log(f"Found {len(followers)} followers for [bold blue]{target_username}[/]")
        
        # Save usernames to file
        with open(RESULT_FILE, 'a') as file:
            for username in followers:
                file.write(username + "\n")

        processed.add(target_username)

        # Recursively process followers
        for follower in followers:
            dump_usernames(follower, depth + 1, max_depth, processed)

    except Exception as e:
        console.log(f"[red]Error processing {target_username}: {str(e)}[/]")

# Entry point
if __name__ == "__main__":
    target_username = input("Masukkan username target: ")
    max_depth = int(input("Masukkan kedalaman pencarian (contoh: 2): "))
    dump_usernames(target_username, max_depth=max_depth)
    console.log("[green]Selesai! Semua username telah disimpan ke file.[/]")
