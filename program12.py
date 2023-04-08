import pandas as pd
df1 = pd.DataFrame([('Raj', "GSS", "CS", 7.2), ('bhagat', "GSS", "stats", 9.6),('jay',"GSBB", "logistics", 98.8)],
                    columns=['Name', 'School', 'Dept.', 'CGPA'])
df2 = pd.DataFrame([('chawla', "GSHS", "Politics", 6.5), ('Teresa', "gshs", "Maths", 9.8)],
                  columns=['Name', 'School', 'Dept.', 'CGPA'])
print(df1)
print()
print(df2)
print()

df3=pd.concat([df1,df2],axis=0,ignore_index=True)

print(df3)
print()

new_row = pd.DataFrame([('sardar', "GSS", "CS", 7.2)], columns=['Name', 'School', 'Dept.', 'CGPA'])

df4 = pd.concat([df3, new_row], ignore_index=True)

print(df4)

new_col=pd.Series(["GITAM", "GITAM", "GITAM", "GITAM", "GITAM", "GITAM"],name="college")

df5 = pd.concat([df4, new_col], axis=1)

print()
print(df5)