import requests
import matplotlib.pyplot as plt
from collections import Counter

# Function to fetch repositories for a user
def fetch_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    return response.json()

# Function to analyze programming languages
def analyze_languages(repos):
    languages = []
    for repo in repos:
        if 'language' in repo and repo['language'] in ['C', 'C#', 'Java']:
            languages.append(repo['language'])
    return Counter(languages)

# Function to generate a bar chart
def generate_bar_chart(language_count):
    languages = list(language_count.keys())
    counts = list(language_count.values())

    plt.bar(languages, counts)
    plt.xlabel('Programming Languages')
    plt.ylabel('Number of Repositories')
    plt.title('Repository Language Statistics')
    plt.savefig('language_statistics.png')
    plt.close()

# Main function
if __name__ == '__main__':
    username = 'Deckster-Lorenzo'
    repos = fetch_repositories(username)
    language_count = analyze_languages(repos)
    generate_bar_chart(language_count)
    print('Language statistics updated and chart generated.')