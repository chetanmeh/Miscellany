# After editing 'sb.json' dump contents into a new python script
# Usually all you will need to do is copy and paste the widgets section
# Then change lowercase 'true' to True, 'false' to False, and 'null' to ""​

from datadog import initialize, api
import json

options = {
    'api_key': '<key_here>',
    'app_key': '<key_here>'
}

initialize(**options)

json_data=open("tb.json").read()
timeboard = json.loads(json_data)

print(timeboard)

board_title = "new_title"

new = api.Timeboard.create(
    title=board_title,
    description=timeboard['dash']['description'],
    template_variables=timeboard['dash']['template_variables'],
    graphs=timeboard['dash']['graphs']
)

print(new)