# After editing 'sb.json' dump contents into a new python script
# Usually all you will need to do is copy and paste the widgets section
# Then change lowercase 'true' to True, 'false' to False, and 'null' to ""​ 

from datadog import initialize, api
import json

options = {
    'api_key': 'key here',
    'app_key': 'key here'
}

initialize(**options)

json_data=open("sb.json").read()
screenboard = json.loads(json_data)

print(screenboard)

board_title = "runtime-openwhisk-v4"

new = api.Screenboard.create(
    board_title=board_title,
    widgets=screenboard['widgets'],
    template_variables=screenboard['template_variables'],
    height=screenboard['height'],
    width=screenboard['width']
)

print(new)