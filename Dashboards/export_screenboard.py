# Export screenboard and save JSON to new file named 'sb.json' in the 
# same directory

from datadog import initialize, api
import json

options = {
    'api_key': 'c086441f807d722a33581be620f0fe6b',
    'app_key': '77c3ff4b62a550496d0a93cd126d26675dc23f3e'
}

initialize(**options)

sb = api.Screenboard.get(582787)
file = open("sb.json", "w")
file.write(json.dumps(sb, indent=4, sort_keys=True))
