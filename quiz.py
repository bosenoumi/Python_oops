import member1
import member2
import member3

#THE SCORING LOGIC EXECUTED THROUGH QUIZ 

# THE SCORING LOGIC EXECUTED THROUGH QUIZ

score = {
    "Technology": 0,
    "Healthcare": 0,
    "Humanities": 0,
    "Commerce": 0,
}

print("\n--- QUICK SKILL & INTEREST QUIZ ---")

# Question 1
print("Q1: How do you prefer to solve problems?")
print("a) Writing code or fixing technical systems")
print("b) Helping people or understanding biological systems")
print("c) Analyzing historical texts, art, or human behavior")
print("d) Managing money, budgets, or business strategies")

q1_choice = input("Your answer (a/b/c/d): ").lower()

if q1_choice == "a":
  score["Technology"] += 10
elif q1_choice == "b":
  score["Healthcare"] += 10
elif q1_choice == "c":
  score["Humanities"] += 10
elif q1_choice == "d":
  score["Commerce"] += 10

# Find the category with the highest points
winning_category = max(score, key=score.get)

print(
    f"\nBased on your quiz score, your top matching path is: {winning_category}"
)


print("That's an end to our career compass journey")
print ( "Have a great professional future ahead!!! All the best !!!")