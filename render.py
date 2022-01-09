import json

import chevron

with open('template.mustache', 'r') as f:
    template_vim = f.read()

with open('spacegray-dark.json', 'r') as f:
    def_dark = json.load(f)

with open('spacegray-light.json', 'r') as f:
    def_light = json.load(f)

with open('colors/sublimetext-spacegray-dark.vim', 'w') as f:
    print(chevron.render(template_vim, def_dark), file=f)

with open('colors/sublimetext-spacegray-light.vim', 'w') as f:
    print(chevron.render(template_vim, def_light), file=f)
