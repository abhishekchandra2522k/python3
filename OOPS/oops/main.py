from user import User
from post import Post

app_user1 = User("user@yahoo.in", "Yajos", "usr99", "Soft Skill Teacher")
app_user1.get_user_info()

app_user1.change_job_title("Instructor")
app_user1.get_user_info()

app_user2 = User("aa@aa.in", "AA", "user2", "Top C++ Instructor")
app_user2.get_user_info()

post1 = Post("on a secret mission to become a ...", app_user2.name)
post1.get_post_info()