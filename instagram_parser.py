from bs4 import BeautifulSoup


def extract_followers(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    followers = set()

    for link in soup.find_all("a"):
        username = link.text.strip()

        if username:
            followers.add(username)

    return followers


def extract_following(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    following = set()

    for heading in soup.find_all("h2"):
        username = heading.text.strip()

        if username:
            following.add(username)

    return following


def get_non_followers(followers_file, following_file):
    followers = extract_followers(followers_file)
    following = extract_following(following_file)

    non_followers = sorted(following - followers)

    return {
        "followers_count": len(followers),
        "following_count": len(following),
        "non_followers_count": len(non_followers),
        "non_followers": non_followers
    }


print("NEW PARSER LOADED")