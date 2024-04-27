from faker import Faker
import psycopg2
import random

# Підключення до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="localhost"
)
cur = conn.cursor()

fake = Faker()

# Функція для заповнення таблиці users
def seed_users(num_records):
    for _ in range(num_records):
        fullname = fake.name()
        email = fake.email()

        # Вставка запису в таблицю users
        cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Функція для заповнення таблиці tasks
def seed_tasks(num_records):
    # Отримання списку всіх user_id з таблиці users
    cur.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cur.fetchall()]

    for _ in range(num_records):
        title = fake.sentence(nb_words=6)
        description = fake.text()
        status_id = random.randint(1, 3)  # Випадковий статус з існуючих
        user_id = random.choice(user_ids)  # Випадковий user_id з таблиці users

        # Вставка запису в таблицю tasks
        cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                    (title, description, status_id, user_id))

# Заповнення таблиць випадковими даними
num_users = 10  # Кількість користувачів
num_tasks = 20  # Кількість завдань
seed_users(num_users)
seed_tasks(num_tasks)

# Збереження змін у базі даних та закриття підключення
conn.commit()
cur.close()
conn.close()
