from app import app, db, Bird

sample_birds = [
    Bird(species='Bald Eagle', location='Minnesota', endangered=True),
    Bird(species='Hummingbird', location='Tropical Park', endangered=False),
    Bird(species='Macaw', location='Rainforest Reserve', endangered=True),
    Bird(species='Owl', location='Old Barn', endangered=False),
]

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Avoid duplicating seeds if run multiple times
        existing = Bird.query.count()
        if existing:
            print(f"Database already has {existing} birds — skipping seed.")
        else:
            for b in sample_birds:
                db.session.add(b)
            db.session.commit()
            print(f"Seeded {len(sample_birds)} birds into the database.")
