import requests

# Replace with your API key and custom search engine ID
api_key = "AIzaSyCfeqsOaWOL0GaYe-MH8rsVCjyZwdJIVQw"
cx = "80319f6d487284922"

u="fossil.com"
dork1 = f"site:{u} ext:log | ext:txt | ext:conf | ext:cnf | ext:ini | ext:env | ext:sh | ext:bak | ext:backup | ext:swp | ext:old | ext:~ | ext:git | ext:svn | ext:htpasswd | ext:htaccess"
dork2 = f"site:{u} -www -shop -share -ir -mfa"
dork3 = f"inurl:q= | inurl:s= | inurl:search= | inurl:query= | inurl:keyword= | inurl:lang= inurl:& site:{u}"


# Number of pages to fetch
num_pages = 5
results_per_page = 10  # Number of results per page

all_urls = []

for page in range(1, num_pages + 1):
    start = (page - 1) * results_per_page + 1

    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={dork1}&start={start}"

    response = requests.get(url)
    print(response.text)
    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])
        urls = [item["link"] for item in items]
        all_urls.extend(urls)
    else:
        print(f"Failed to retrieve search results for page {page}")

# Print all the retrieved URLs
for url in all_urls:
    print(url)
