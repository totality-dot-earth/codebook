import json

out = []
x = {
    'feature_class': '',
    'super_class': '',
    'description': ''
}
with open('mtfccs2019.txt') as fd:
    item = None
    for line in fd:
        code = line[0:5]
        if code.strip() != '':
            # start line
            if item:
                item['feature_class'] = item['feature_class'].strip()
                item['super_class'] = item['super_class'].strip()
                item['description'] = item['description'].strip()
                out.append(item)
            item = x.copy()
            item['code'] = code
            item['point'] = line[64:67].strip()
            item['linear'] = line[71:74].strip()
            item['areal'] = line[80:83].strip()
        item['feature_class'] += ' ' + line[6:36].strip()
        item['super_class'] += ' ' + line[37:60].strip()
        item['description'] += ' ' + line[88:].strip()

with open('mtfccs2019.json', 'w') as fd:
    fd.write(json.dumps(out, indent=2))

with open('mtfccs2019.tsv', 'w') as fd:
    for item in out:
        fd.write('\t'.join(
            [item['code'], item['super_class'], item['feature_class'],
             item['point'], item['linear'], item['areal'], item['description']]) + '\n')
