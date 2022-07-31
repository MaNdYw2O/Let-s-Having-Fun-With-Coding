

#for Choosing random choices and Random value Generation
import random

#Our list of Places where we Want to Go

Places = ["Rajasthan tourism",
"Kerala",
"Amritsar",
"Kashmir tour",
"Mumbai",
"Gujraat",
"Patna",
"Lucknow",
"Vridavan",
"Goa"]

#Lists of Random Friends

Friends = ["Rudra",
"Christine",
"Arjun Pandit",
"Manjeet",
"Aadu",
"Mridul",
"Shanu",
"Shanvi",
"Jestina",
"Pushpinder ", "Future Friends"]

# Lists Of Things We Want to experience

experience = ["Adventure", "Love", "Thrill", "Suspense", "Equality", "Kindness", "Simplicity", "Understanding", "Helping Hand"]



random_places = random.choice(Places) 
random_friend = random.choice(Friends)
random_experience = random.choice(experience)

print(f"How about you to go {random_places} with {random_friend} and experience some {random_experience}?")