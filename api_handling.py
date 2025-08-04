import requests

# def fetch_random_activity():
#     print("\n🎲 Activity Suggestion:")
#     try:
#         res = requests.get("https://www.boredapi.com/api/activity")
#         res.raise_for_status()
#         data = res.json()
#         print(f"➡️ {data['activity']} (Type: {data['type']})")
#     except:
#         print("❌ Couldn't fetch activity.")


def fetch_chuck_norris_joke():
    print("\n😂 Chuck Norris Joke:")
    try:
        res = requests.get("https://api.chucknorris.io/jokes/random")
        res.raise_for_status()
        joke = res.json().get("value", "No joke found.")
        print(f"💬 {joke}")
    except:
        print("❌ Couldn't fetch joke.")


def fetch_cat_fact():
    print("\n🐱 Cat Fact:")
    try:
        res = requests.get("https://catfact.ninja/fact")
        res.raise_for_status()
        fact = res.json().get("fact", "No fact found.")
        print(f"📘 {fact}")
    except:
        print("❌ Couldn't fetch cat fact.")


def fetch_random_dog_image():
    print("\n🐶 Random Dog Image URL:")
    try:
        res = requests.get("https://dog.ceo/api/breeds/image/random")
        res.raise_for_status()
        image_url = res.json().get("message", "No image found.")
        print(f"📸 {image_url}")
    except:
        print("❌ Couldn't fetch dog image.")


def show_api_magic():
    print("\n✨ API Magic Showcase ✨")
    print("=" * 35)
#     fetch_random_activity()
    fetch_chuck_norris_joke()
    fetch_cat_fact()
    fetch_random_dog_image()
    print("=" * 35)
    print("🎉 Done! Hope that made you smile.\n")


if __name__ == '__main__':
    show_api_magic()
