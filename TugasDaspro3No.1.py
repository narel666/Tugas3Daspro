info_login = [
    {'username': 'nabila', 'password': '1989'},
    {'username': 'nabil', 'password': '2005'},
    {'username': 'safril', 'password': '2004'},
    {'username': 'ilham', 'password': '2005'},
    {'username': 'agung', 'password': '2001'},
    {'username': 'amir', 'password': '1999'},
    {'username': 'arridho', 'password': '2004'},
    {'username': 'gatshu', 'password': '2004'},
    {'username': 'rizal', 'password': '2004'},
    {'username': 'destito', 'password': '2004'},
]

# Input username dan password
username = input('Masukkan Username: ')
password = input('Masukkan Password: ')

# Loop untuk memeriksa setiap entri dalam info_login
for data in info_login:
    if data['username'] == username and data['password'] == password:
        print('Welcome', username)
        break  # Menghentikan loop jika kombinasi username dan password cocok
else:
    print('Username atau password salah')
