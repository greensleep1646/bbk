import requests

def get_user_info(username):
    url = f"https://api.telegram.org/bot{TOKEN}/getUserProfilePhotos?user_id={username}"
    response = requests.get(url)
    return response.json()

def get_user_location(username):
    url = f"https://api.telegram.org/bot{TOKEN}/getUserLocation?user_id={username}"
    response = requests.get(url)
    return response.json()

def main():
    username = input("Telegram kullanıcı adını girin: ")
    user_info = get_user_info(username)
    user_location = get_user_location(username)

    if user_info and user_location:
        print("Kullanıcı adı: ", user_info["result"][0]["user_id"])
        print("Konum: ", user_location["result"]["longitude"], ", ", user_location["result"]["latitude"])
    else:
        print("Kullanıcı bulunamadı!")

if name == "main":
    main()
