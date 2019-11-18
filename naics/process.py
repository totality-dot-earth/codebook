import csv
import json

levels = {
    2: 'sector',
    3: 'subsector',
    4: 'industry group',
    5: 'industry',
    6: 'national industry'
}


#  dP                              dP   
#  88                              88   
#  88 88d888b. 88d888b. dP    dP d8888P 
#  88 88'  `88 88'  `88 88    88   88   
#  88 88    88 88.  .88 88.  .88   88   
#  dP dP    dP 88Y888P' `88888P'   dP   
#              88                       
#              dP                       

# read code titles
codes = {}
with open('orig/2-6 digit_2017_Codes.csv') as fd:
    rd = csv.reader(fd)
    next(rd)
    next(rd)
    for line in rd:
        code = line[1].strip()
        title = line[2].strip()
        codes[code] = {
            'code': code,
            'title': title,
            'level': levels[len(code)]
        }

# read in code descriptions
with open('orig/2017_NAICS_descriptions.csv') as fd:
    rd = csv.reader(fd)
    next(rd)
    for line in rd:
        code = line[0].strip()
        description = line[2]
        codes[code]['description'] = description

# Note: this recursion assumes that parents are added before children,
# which is true for the official data release
hierarchy = {
    'code': '_',
    'children': []
}
def add_to_hierarchy(item, current):
    if len(item['code']) == 2 or len(item['code']) == len(current['code']) + 1:
        # attach as child
        if 'children' not in current:
            current['children'] = []
        current['children'].append({
            'code': item['code']
        })
    else:
        # search children for attachment point
        for new in current.get('children', []):
            if item['code'].startswith(new['code']):
                add_to_hierarchy(item, new)

for _, item in codes.items():
    add_to_hierarchy(item, hierarchy)


#   .88888.             dP                       dP   
#  d8'   `8b            88                       88   
#  88     88 dP    dP d8888P 88d888b. dP    dP d8888P 
#  88     88 88    88   88   88'  `88 88    88   88   
#  Y8.   .8P 88.  .88   88   88.  .88 88.  .88   88   
#   `8888P'  `88888P'   dP   88Y888P' `88888P'   dP   
#                            88                       
#                            dP                       

def output_children(item):
    if 'children' in item:
        cs = ','.join([it['code'] for it in item['children']])
        fd.write(f"{item['code']}\t{cs}\n")
        [output_children(c) for c in item['children']]

with open('2017_NAICS_children.tsv', 'w') as fd:        
    output_children(hierarchy)

with open('naics_2017_codes.json', 'w') as fd:
    fd.write(json.dumps(codes, indent=2))

with open('naics_2017_hierarchy.json', 'w') as fd:
    fd.write(json.dumps(hierarchy, indent=2))