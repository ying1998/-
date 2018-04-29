from admin import Admin

myadmin = Admin(first_name="yingcheng",last_name="yingtuo")
myadmin.describe_user()
myadmin.privileges.show_privileges()

myadmin['jen'] = 'python'

print(myadmin['jen'])
