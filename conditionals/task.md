University Admission Decision — Core Logic Challenge

Write a Python program that asks for:

1. UTME score
2. Post-UTME score
3. O'level result available? (yes/no)
4. Number of O'level credits
5. Age
6. Number of previous admission attempts


Admission Requirements

A candidate must satisfy the following:

1. UTME

UTME must be at least 180.
If UTME is 180–199, the candidate is automatically rejected.
If UTME is 200–219, Post-UTME must be at least 60.
If UTME is 220–279, Post-UTME must be at least 50.
If UTME is 280 or above, Post-UTME must be at least 45.


2. O'level

O'level result must be available.
Candidate must have at least 5 credits.
If the candidate has exactly 5 credits, they must have a UTME score of at least 220.
If they have 6 or more credits, the normal UTME requirement applies.


3. Age

Age ≤ 25 → normal eligibility.
Age 26–27 → candidate must have UTME ≥ 250.
Age > 27 → automatically rejected.


4. Previous Attempts

0–2 previous attempts → no restriction.
3–4 attempts → candidate must have UTME ≥ 220.
More than 4 attempts → candidate is rejected.

🧠 Final Decision

The program should determine whether the candidate is:
ADMITTED
or
REJECTED

If rejected, it should display every requirement they failed, not just the first one.

For example:

REJECTED

Reasons:
- Post-UTME score is below the required score.
- O'level result is not available.
- Age exceeds the maximum permitted age.

Extra Challenge

Add a WAITLISTED category.

A candidate is WAITLISTED if they fail exactly one non-automatic requirement.

For example:

UTME: 215
Post-UTME: 55
O'level: Yes
Credits: 6
Age: 23
Attempts: 1

They would be waitlisted because their UTME is 200–219 and therefore requires a Post-UTME score of 60.

But someone who is 28 years old should be immediately:

REJECTED
- Age exceeds the maximum permitted age.
because age > 27 is an automatic rejection.

🔒 Restrictions

For the first attempt, use only:

input()
if
elif
else
and
or
not

No loops, lists, functions, dictionaries, or libraries.