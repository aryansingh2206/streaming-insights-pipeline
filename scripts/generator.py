import pandas as pd
import random
from faker import Faker
from datetime import timedelta
import os

fake = Faker()

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

genres = [
    "Action", "Drama", "Comedy", "Sci-Fi",
    "Thriller", "Romance", "Horror"
]

shows = {
    "Action": ["Extraction", "Vikings", "Narcos"],
    "Drama": ["Breaking Bad", "The Crown", "Ozark"],
    "Comedy": ["Friends", "The Office", "Brooklyn 99"],
    "Sci-Fi": ["Dark", "Stranger Things", "Black Mirror"],
    "Thriller": ["Mindhunter", "You", "Money Heist"],
    "Romance": ["Bridgerton", "Emily in Paris", "Virgin River"],
    "Horror": ["The Haunting", "Fear Street", "Ghoul"]
}

rows = []

print("Generating 5000 fake streaming logs...")

for _ in range(5000):
    genre = random.choice(genres)
    show = random.choice(shows[genre])

    start_time = fake.date_time_between(start_date='-7d', end_date='now')
    duration = random.randint(5, 90)  # minutes
    end_time = start_time + timedelta(minutes=duration)

    rows.append({
        "user_id": fake.uuid4(),
        "genre": genre,
        "show": show,
        "start_time": start_time,
        "end_time": end_time,
        "duration_min": duration
    })

df = pd.DataFrame(rows)
df.to_csv("data/logs.csv", index=False)

print("Done! Saved to data/logs.csv")
