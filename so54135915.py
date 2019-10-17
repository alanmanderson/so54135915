content = ''
with open('test.out', 'r') as f:
  for line in f:
    if line.startswith('#'): continue
    content += line

with open('test.out', 'w') as f:
  f.write(content)
