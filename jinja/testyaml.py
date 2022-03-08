import ruamel.yaml
yaml = ruamel.yaml.YAML()
#Load the yaml files
with open('./test1.yml') as f:
    data = yaml.load(f)
data= dict(data)
with open('./test2.yml') as fp:
    data1 = yaml.load(fp)
data1=dict(data1)
#Add the resources from test2.yaml to test1.yaml resources
#data['stages']['jobs'].update(data1)

print(data)
print('***************************************************')
print(data1)
