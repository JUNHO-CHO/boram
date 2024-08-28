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

## 1. Account [membership function]
- Membership: Users can create an account with their ID and password.
- Login: Existing users can log in with their registered ID and password.
- Logout: Users can safely terminate their accounts by logging out.
- Modifying membership information: Users can update their account information.
- Withdrawal from membership: If the service is no longer available, the user can delete the account.

### 🖥️ Run a program
#### Login page brightness adjust mode
|Bright|Dark|
|----|----|
|<img src="https://github.com/user-attachments/assets/77ad8178-5521-470a-92a3-2e2982bbdd00" width="300">|<img src="https://github.com/user-attachments/assets/07d7809b-1989-4656-8cf4-a81cb4e6870f"  width="300">|

####

----
## 2. Article [publishing function]
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

### 🖥️ Run a program
#### Bulletin board page brightness mode dark mode
|Bright|Dark|
|----|----|
|<img src="https://github.com/user-attachments/assets/78de4b5b-520e-4508-8596-a4c1784bfda4" width="300">|<img src="https://github.com/user-attachments/assets/5c7f71d8-29ab-4693-9511-26269bf6ce27"  width="300">|

#### Sort by latest order, old order, popularity order
|Sorting|Example: Sorting in old order|
|----|----|
|<img src="https://github.com/user-attachments/assets/7ad77668-fde5-4f35-83e4-9627e3206473" width="300">|<img src="https://github.com/user-attachments/assets/810d2779-8f3f-4c47-9d8d-9ab36e5685d8" width="300">|

#### Search function
|Bright|Dark|
|----|----|
|<img src="https://github.com/user-attachments/assets/0f084c29-d460-4f68-af04-47036ad1d3a1" width="300">|<img src="https://github.com/user-attachments/assets/0e90e328-e3c6-4792-9b6d-020355cbe466" width="300">|

#### registration function
|Bright|Dark|
|----|----|
|<img src="https://github.com/user-attachments/assets/2e5ad91f-cd3a-4656-9007-0adf181174ae" widh="300>|<img src="https://github.com/user-attachments/assets/2c8b92b4-39e9-4e05-a89e-c61863215190" width="300">|

#### Inquiry of the article written by the user himself/herself
|Bright|Dark|
|----|----|
|<img src="https://github.com/user-attachments/assets/a4c6e44f-f855-4523-937e-9e2ded723fee" widh="300">|<img src="https://github.com/user-attachments/assets/0b1c6654-cb32-4a45-aea5-139e89e48173" widh="300">|

#### Inquire articles written by other users
|Bright|Dark|
|----|----|
|<img src="https://github.com/user-attachments/assets/32e40626-72b2-43d7-8e1b-265a1057f488" width="300">|<img src="https://github.com/user-attachments/assets/5aea381e-f7ac-4d7a-9097-92fc69938e5c" width="300">|

#### Various functions
|Additional actions when writing your own posts|Likes & Views|Hashtag|
|----|----|----|
|<img src="https://github.com/user-attachments/assets/f96bfc6b-8866-4b7c-ab6e-6f4d30872edb" width="150">|<img src="https://github.com/user-attachments/assets/a7f3fc22-c77d-4372-8f94-8d2165ca7d85" width="150">|<img src="https://github.com/user-attachments/assets/9b79f128-01eb-409f-8355-5a23346bb85d" width="150">|

#### Ability to add posts made by other users
|Bright|Dark|
|----|----|
|<img src="https://github.com/user-attachments/assets/7de1d38f-5889-4b8f-87bc-b3efa00e593a" width="200">|<img src="https://github.com/user-attachments/assets/83891760-310c-4c79-84b3-0dd810ee9df2" width="200">|

#### Notification window when deleting
|Bright|Dark|
|----|----|
|<img src="https://github.com/user-attachments/assets/64841549-7051-4a4f-94d9-85532c16f509" width="200">|<img src="https://github.com/user-attachments/assets/5a0353b9-0856-4ea9-ba24-f714e06adcdb" width="200">

----
## 3. User [User Features]
- Profile page: Users can view their profiles.
- Username—Displays the name of the user.
- Subscription Date—Displays the subscription date for the user.
- Registered Items: You can view the posts you have registered.
- Steamed items: You can check the posts you've picked up.
- Follow function: You can follow specific users, and you can check the follower/follow list.
- Follow: Users follow others.
- Followers: You can view a list of people who follow you.

----
# 📄ERD Diagram
![ERD](https://github.com/user-attachments/assets/00db2583-9f10-4420-88e5-e1baefadeadb)

