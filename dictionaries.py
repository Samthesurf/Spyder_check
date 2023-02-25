# 'htanaka' = 'full_name' = "Haru Tanaka"
# ppatel.full_name = 'Priya Patel'
# ppatel.year_hired= 2015
# ppatel.dependents = 1
# ppatel.has_company_cell=True
ppatel = {'full_name':'Priya Patel',
            'year_hired':2015,
            'dependents':1,
            'has_company_cell':True}
print(type(ppatel))
print(ppatel)
for info in ppatel.keys():
    print(f'{info} = {ppatel[info]}')