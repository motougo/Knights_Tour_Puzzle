def solve():
    # Write your code here
    real_password = wrong_password(0)
    print(real_password)
    return real_password


def wrong_password(password):
    real_password = 'mark ugolini'
    return (password == "" or (not password and real_password)) or password != real_password

