 # 🪷 BORAM 🪷

# ⏰ Development Period
- 2024.08.14 ~ 2024.08.28
----
# 👩🏻‍💻 Project Introduction

Through the Sparta Coding Club Bootcamp, team assignments were carried out on the theme of Sparta Market.


A basic second-hand transaction web using Django was implemented, and the actual purchased function and regional classification were not implemented.


It is a platform that allows users to register transaction items of used products and express their interest through 'likes' of items registered by other users.

In addition, users can easily check their registered products by following their favorite sellers.

----
# 💻 Development Environment

|Programming Language| python 3.10|
|:----------------:|:----------------:|
| Web Framework | Django 4.2|
| Database | SQLite|
| IDE | PyCharm, Vs code |
| Version Control | Git, Github |
| Communication | Zep, Notion, Slack|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap, JS |
| Database | Django ORM, SQLite |

----
# 🧑‍🧑‍🧒‍🧒 Developement Team

[🔗 boram-notion](https://teamsparta.notion.site/b1f541f0549f4e7f9e07c9cc547f1ec6)

#### 👑 Cho Jun-ho(Team Leader)
- membership function
- Hashtag
- presentation of ppt materials

#### 👤 Kang Ji-seok
- membership function
- Posting css
- Search Features
- Create Readme

#### 👤 Kim Na-hyeon
- publishing function
- User Features
- Create Readme and erd

#### 👤 Jeon Min-sung
- publishing function
- User Features
- Base, Login css
- Full functionality, error correction and design completion
- Project Demonstration and Editing
----

# 🧬 Directory Structure
| Structure| Function|
|----------------|----------------|
| accounts | User authentication and account management capabilities |
| articles | Create, modify, delete, and search posts (objects) |
|  media | Save uploaded image file |
| spartamarket | Project Settings and Initialization Files |
| static | Static files (CSS, JS, images, etc.) |
| templates | Common Django template files |
| users | User Profiles and Follow Features|

----
# 📌 Project Features

### Account [membership function]
- Membership: Users can create an account with their ID and password.
- Login: Existing users can log in with their registered ID and password.
- Logout: Users can safely terminate their accounts by logging out.
- Modifying membership information: Users can update their account information.
- Withdrawal from membership: If the service is no longer available, the user can delete the account.

### Article [publishing function]
- Writing and registering: Users can create and post descriptions of objects.
- Revise text: You can modify the content of your registered text.
- Delete text: Users can delete their posts.
- Individual Detail Page (Writing Lookup): Users can look up the details of a particular post.
- Sort posts: You can sort posts in the order of latest, old, and popularity.
- View: You can see how many views your post has been viewed.
- Steaming (like): Users can steam a post they are interested in.
- Hashtags: You can add hashtags to posts to increase their relevance.
- Search function: You can search for posts by various criteria.
- Subject: Search based on the title of the post.
- Item Description: Search based on the item description in the post.
- Member name: Search based on the author's name.
- Hashtags: Search with hashtags.

### User [User Features]
- Profile page: Users can view their profiles.
- Username—Displays the name of the user.
- Subscription Date—Displays the subscription date for the user.
- Registered Items: You can view the posts you have registered.
- Steamed items: You can check the posts you've picked up.
- Follow function: You can follow specific users, and you can check the follower/follow list.
- Follow: Users follow others.
- Followers: You can view a list of people who follow you.

|Features|execute a function|
|--------|--------|
|Account|![image](https://github.com/user-attachments/assets/13feeb32-6e43-4268-8a2c-e60c2164112c)|

----
# 📄ERD Diagram
![ERD](https://github.com/user-attachments/assets/00db2583-9f10-4420-88e5-e1baefadeadb)

