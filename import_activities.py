
import aiosqlite
import asyncio
import csv
from config import DB_PATH

async def import_activities_from_csv():
    async with aiosqlite.connect(DB_PATH) as db:
        with open("import_activities.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            activities = [
                (
                    row["title"],
                    row["description"],
                    row["weather"],
                    row["mood"],
                    row["budget"],
                    row["duration"]
                )
                for row in reader
            ]

        await db.executemany('''
            INSERT INTO activities (title, description, weather, mood, budget, duration)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', activities)

        await db.commit()
        print(f"Импортировано {len(activities)} активностей.")

if __name__ == "__main__":
    asyncio.run(import_activities_from_csv())
