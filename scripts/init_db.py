#!/usr/bin/env python3
"""
Database initialization script
"""

from app.core.database import Base, engine
from app.models import item


def init_db():
    """Initialize the database"""
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")


if __name__ == "__main__":
    init_db()
