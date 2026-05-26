class User:
	def __init__(self, user_id, username):
		self.id = user_id
		self.username = username
		self.followers = 0
		self.following = 0

	def follow(self, user):
		user.followers += 1
		self.following += 1
		print(f"Now Following {user.username}!")

	def describe(self):
		print(f"UserID: {self.id}, Username: {self.username}, Followers: {self.followers}, Following: {self.following}")

user_1 = User("007", "Bond")
user_2 = User("01", "Michael")

user_1.describe()

user_1.follow(user_2)

user_1.describe()
user_2.describe()