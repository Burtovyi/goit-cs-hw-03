from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до MongoDB
client = MongoClient('localhost', 27017)
db = client['cats_database']
collection = db['cats_collection']

# Читання (Read)

def get_all_cats():
    """Функція для виведення всіх записів із колекції."""
    cats = collection.find({})
    for cat in cats:
        print(cat)

def get_cat_by_name(name):
    """Функція, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота."""
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Кіт з таким ім'ям не знайдений.")

# Оновлення (Update)

def update_cat_age(name, new_age):
    """Функція, яка дозволяє користувачеві оновити вік кота за ім'ям."""
    collection.update_one({"name": name}, {"$set": {"age": new_age}})
    print("Вік кота оновлено.")

def add_cat_feature(name, new_feature):
    """Функція, яка дозволяє додати нову характеристику до списку features кота за ім'ям."""
    collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    print("Нову характеристику додано.")

# Видалення (Delete)

def delete_cat_by_name(name):
    """Функція для видалення запису з колекції за ім'ям тварини."""
    collection.delete_one({"name": name})
    print("Кіт видалено.")

def delete_all_cats():
    """Функція для видалення всіх записів із колекції."""
    collection.delete_many({})
    print("Усіх котів видалено.")

if __name__ == "__main__":
    # Приклади викликів функцій:
    get_all_cats()
    get_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_cat_feature("barsik", "любить спати")
    delete_cat_by_name("barsik")
    delete_all_cats()
