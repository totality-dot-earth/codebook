# https://www.census.gov/population/estimates/metro-city/List6.txt

# 1-3             3       Three-digit Combined Statistical Area code (November 2004 definition)
# 4-5             2       Blank
# 6-10            5       CBSA code (blank at CSA level)
# 11-12           2       Blank
# 13-88           75      CSA Area Title
# 16-88           73      CBSA Title

import json 

with open('csa-cbsa.txt') as fd:
    data = []
    for line in fd.readlines():
        csa_token = line[0:3]
        try:
            int(csa_token)
        except ValueError as e:
            # one of the documentation lines in the original file
            continue
        
        cbsa_token = line[5:10].strip()
        if cbsa_token is '':
            # CSA line
            csa_title = line[12:88]
            cbsa_title = ''
        else:
            # CBSA line
            csa_title = ''
            cbsa_title = line[15:88]
        
        d = {
            'csa_code': csa_token,
            'cbsa_code': cbsa_token,
        }
        if cbsa_token is '':
            d['type'] = 'csa'
            d['title'] = csa_title
        else:
            d['type'] = 'cbsa'
            d['title'] = cbsa_title
        data.append(d)

with open('csa-cbsa.psv', 'w') as out:
    for d in data:
        out.write('|'.join([d['type'], d['csa_code'], d['cbsa_code'], d['title']]))

with open('csa.tsv', 'w') as out:
    for d in data:
        if d['type'] == 'csa':
            out.write(f"{d['csa_code']}\t{d['title']}")

with open('cbsa.tsv', 'w') as out:
    for d in data:
        if d['type'] == 'cbsa':
            out.write(f"{d['cbsa_code']}\t{d['title']}")

with open('csa-cbsa.json', 'w') as out:
    out.write(json.dumps(data, indent=2))

        