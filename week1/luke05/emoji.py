import re
import sys
import requests

# {"error":false,
# "state":"[>🍕<, 🍉, 🐴, 🐟, 🚀, 🚩]",
# "message":"Tilgjengelig ,n🚽er: ✨, ⚡, 🔑, 🤷. Eksempel: /api/🙃.js?commands=✨⚡✨"}
# emojis = ['✨', '⚡', '🔑', '🤷']

# Start bruteforcing
for s in range(6):
    for l in range(6):
        c = ['✨', '⚡']
        key = c[0]*s + c[1]*l
        key = ''.join(key) + '🔑'
        url = f'https://npst.no/api/🙃.js?commands={key}'
        r = requests.get(url)
        if 'PST' in r.text:
            flag = re.search('PST\{.*?\}', r.text).group()
            print(f'\n{key}: {flag}\n')
            sys.exit(0)
        
        key = c[1]*s + c[0]*l
        key = ''.join(key) + '🔑'
        url = f'https://npst.no/api/🙃.js?commands={key}'
        r = requests.get(url)
        if 'PST' in r.text:
            flag = re.search('PST\{.*?\}', r.text).group()
            print(f'\n{key}: {flag}\n')
            sys.exit(0)