from models import Challenge

all_challenges = Challenge.select()

Challenge.create(language="Ruby", name="Booleans")

sorted_challenges = Challenge.select().order_by(Challenge.steps)