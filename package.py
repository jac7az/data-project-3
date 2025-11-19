import requests
import os
import sys

GITHUB_TOKEN=os.getenv("")
GITHUB_AUTH_HEADER={"Authorization": "token".format(GITHUB_TOKEN)} if GITHUB_TOKEN else {}

def get_next_page(page):
    return page if page.headers.get('link')!=None else None
def get_commits(url):   #enter api python package url here
    session=requests.Session()
    url=url
    params={'per_page':100}
    first_page=session.get(url, headers=GITHUB_AUTH_HEADER, params=params)
    yield first_page

    next_page=first_page
    while get_next_page(next_page) is not None:
        try:
            next_page_url=next_page.links['next']['url']
            next_page=session.get(next_page_url, headers=GITHUB_AUTH_HEADER, params=params)
            yield next_page
        except KeyError:
            print("No more pages to fetch.")
            break
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            break
if __name__ == "__main__":
    count=0
    try:
        for page in get_commits("https://api.github.com/repos/pandas-dev/pandas/commits"):  #enter api python package url here
            commits=page.json()
            for commit in commits:
                count+=1
                print(count,' ',commit['sha'])
    except KeyboardInterrupt:
        quota_url="https://api.github.com/rate_limit"
        session=requests.Session()
        quota_response=session.get(quota_url, headers=GITHUB_AUTH_HEADER)
        quota_data=quota_response.json()
