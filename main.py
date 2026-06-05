# Import
import json

# function for load the data
def load_data(file_name):
    with open(file_name,"r") as file:
        data = json.load(file)
    return data


# function which display the user's friends and pages
def about_user(data):
    print("User and his connections\n")
    for user in data['users']:
        print(
            f"User ID : {user['id']} - {user['name']} is friends of : {user['friends']} and he likes the pages : {user['liked_pages']}")
    print("\nAbout page information:")
    for page in data['pages']:
        print(f"{page['id']} : {page['name']} ")


# function for the cleaning the data
def cleaning_data(data):
    # Remove the users with missing names
    data["users"] = [user for user in data["users"] if user["name"].strip()]

    # Remove duplicate friends
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))

    # Remove the inactive users
    data["users"] = [user for user in data["users"] if user["friends"] or user["liked_pages"]]

    # Remove the duplicate pages
    unique_pages = {}
    for pages in data["pages"]:
        unique_pages[pages['id']] = pages
    data['pages'] = list(unique_pages.values())

    return data




# function which give the name of user from his id number
def id_to_user(user_id,data):
    for user in data["users"]:
        if user['id']== user_id:
            return user['name']

# function  which give the page name from page id
def id_to_pages(page_id,data):
    for page in data["pages"]:
        if page['id']== page_id:
            return page['name']


# Friend suggestion function
def peoples_suggestion(user_id, data):
    user_friends = {}
    for user in data["users"]:
        user_friends[user['id']] = set(user['friends'])

    if user_id not in user_friends:
        return []

    direct_friends = user_friends[user_id]
    suggestion = {}
    for friend in direct_friends:
        for mutual in user_friends[friend]:
            if mutual != user_id and mutual not in direct_friends:
                # Count the mutual friends
                suggestion[mutual] = suggestion.get(mutual, 0) + 1
    sorted_suggestion = sorted(suggestion.items(), key=lambda x: x[1], reverse=True)
    return [user_id for user_id, mutual_count in sorted_suggestion]


# function for the page suggestion based on common interest
def suggest_pages(user_id, data):
    # Empty dictionary for user_pages
    user_pages = {}

    for user in data["users"]:
        user_pages[user['id']] = set(user['liked_pages'])  # and these are te values for the keys

    # if the user not found than return the empty list
    if user_id not in user_pages:
        return []

    user_liked_pages = user_pages[user_id]

    page_suggestion = {}

    for other_user, pages in user_pages.items():
        if other_user != user_id:
            shared_pages = user_liked_pages.intersection(pages)
        for page in pages:
            if page not in user_liked_pages:
                page_suggestion[page] = page_suggestion.get('get', 0) + len(shared_pages)

    sorted_pages = sorted(page_suggestion.items(), key=lambda x: x[1], reverse=True)
    return [page_id for page_id, _ in sorted_pages]

def main():

    print("===== USER INFORMATION =====")
    data2 = load_data("data/data2.json")
    about_user(data2)

    print("\n===== DATA CLEANING =====")
    data3 = load_data("data/data3.json")

    cleaned_data = cleaning_data(data3)

    print("\nData cleaned successfully!")
    about_user(cleaned_data)

    print("\n===== FRIENDS SUGGESTION =====")

    data_massive = load_data("data/massive_data.json")

    user_id = 2

    suggestions = peoples_suggestion(user_id, data_massive)

    print(f"\nUser Name : {id_to_user(user_id, data_massive)}")

    print("\nSuggested Friends:")

    for friend in suggestions:
        print(id_to_user(friend, data_massive))

    print("\n===== PAGES SUGGESTION =====")
    suggested_pages = suggest_pages(user_id, data_massive)

    print(f"\nUser Name : {id_to_user(user_id, data_massive)}")

    print("\nSuggested Pages:")

    for page in suggested_pages:
        print(id_to_pages(page, data_massive))


if __name__ == "__main__":
        main()

