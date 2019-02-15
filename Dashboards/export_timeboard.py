# Export screenboard and save JSON to new file named 'sb.json' in the 
# same directory

from datadog import initialize, api
import json

options = {
    'api_key': '<key_here>',
    'app_key': '<key_here>'
}

initialize(**options)

sb = api.Timeboard.get("timeboard-id")
file = open("tb.json", "w")
file.write(json.dumps(sb, indent=4, sort_keys=True))
