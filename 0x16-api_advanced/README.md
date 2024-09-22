# 0x16. API advanced

In this advanced project, I further honed my skills in querying APIs by working with the Reddit API.

## Function Prototypes 💾

Here are the prototypes for the functions developed in this project:

- **0-subs.py:** `def number_of_subscribers(subreddit)`
- **1-top_ten.py:** `def top_ten(subreddit)`
- **2-recurse.py:** `def recurse(subreddit, hot_list=[])`
- **100-count.py:** `def count_words(subreddit, word_list)`

## Tasks 📃

### 0. How Many Subs?
**File:** `0-subs.py`

- **Description:** Returns the total number of subscribers for a given subreddit.
- **Behavior:** Returns `0` if an invalid subreddit is provided.

### 1. Top Ten
**File:** `1-top_ten.py`

- **Description:** Prints the top ten hottest posts for a given subreddit.
- **Behavior:** Prints `None` if an invalid subreddit is provided.

### 2. Recurse it!
**File:** `2-recurse.py`

- **Description:** Recursively returns a list of titles for all hot articles on a given subreddit.
- **Behavior:** Returns `None` if no results are found for the subreddit.

### 3. Count it!
**File:** `100-count.py`

- **Description:** Recursively prints a sorted count of given keywords parsed from titles of all hot articles on a given subreddit.
- **Details:**
  - Keywords are case-insensitive and separated by spaces.
  - Results are printed in descending order by count.
  - Words with identical counts are sorted alphabetically.
  - Words with no matches are skipped.
  - Results are based on the frequency of each keyword (e.g., "java java java" counts as three instances of "java").

---

This format provides a clear and organized overview of the project, function prototypes, and task descriptions.
