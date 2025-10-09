from app import app, db, Bird, Contact

sample_birds = [
    Bird(species='Bald Eagle', location='Minnesota', endangered=True),
    Bird(species='Hummingbird', location='Tropical Park', endangered=False),
    Bird(species='Macaw', location='Rainforest Reserve', endangered=True),
    Bird(species='Owl', location='Old Barn', endangered=False),
]

sample_contacts = [
    Contact(name='John Doe', email='john@example.com', message='I love eagles!', page_origin='brent'),
    Contact(name='Jane Smith', email='jane@example.com', message='Parakeets are my favorite', page_origin='jeremiah'),
    Contact(name='Bob Johnson', email='bob@example.com', message='Bird experience: 5 years of birdwatching', page_origin='mason'),
    Contact(name='Alice Brown', email='alice@example.com', message='Diet', page_origin='garrett')
]

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Seed birds if none exist
        existing_birds = Bird.query.count()
        if existing_birds:
            print(f"Database already has {existing_birds} birds — skipping bird seed.")
        else:
            for b in sample_birds:
                db.session.add(b)
            db.session.commit()
            print(f"Seeded {len(sample_birds)} birds into the database.")
        
        # Seed contacts if none exist
        existing_contacts = Contact.query.count()
        if existing_contacts:
            print(f"Database already has {existing_contacts} contacts — skipping contact seed.")
        else:
            for c in sample_contacts:
                db.session.add(c)
            db.session.commit()
            print(f"Seeded {len(sample_contacts)} contacts into the database.")
