import os
import mysql.connector
import numpy as np
from dotenv import load_dotenv
load_dotenv()

try:
    conn=mysql.connector.connect(host=os.getenv("hostname"),
                                 username=os.getenv("db_username"),
                                 password=os.getenv("password"),
                                 database=os.getenv("databasename")
                                 )
    print("connection successful")
#==========Table1===========
    cursor=conn.cursor()
    cursor.execute("select *from student93;")
    data=cursor.fetchall()
    student=np.array(data)
    #print(data)
    print("\n----------Table 1----------\n")
    print(student)
    print("\n","-"*40,"\n")
#=======marks========
    marks=student[:,3].astype(int)
    print(marks)
    print("\n","-"*40,"\n")
    
    print("Highest marks: ",np.max(marks))
    print("\n","-"*40,"\n")

    print("lowest marks: ",np.min(marks))
    print("\n","-"*40,"\n")

    print("Average: ",np.mean(marks))
    print("\n","-"*40,"\n")

    print("Above Average: ",marks[marks>marks.mean()])
    print("\n","-"*40,"\n")

    print("Below Average: ",marks[marks<marks.mean()])
    print("\n","-"*40,"\n")

    print("Sum: ",np.sum(marks))
    print("\n","-"*40,"\n")

    print("Sort: ",np.sort(marks))
    print("\n","-"*40,"\n")

#========Table2=========
    cursor.execute("select *from student94;")
    table2=cursor.fetchall()
    #print(table2)
    student2=np.array(table2)
    print("---------Table 2----------\n")
    print(student2)
    print("\n","-"*40,"\n")

#========Concatenate===== 
    combine=np.concatenate((student,student2))
    print("----------Table 3-----------\n")
    print(combine)
    print("\n","-"*40,"\n")

#=======Table 3========
    cursor.execute("""CREATE TABLE IF NOT EXISTS student95(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    course VARCHAR(50),
    marks INT
)
""")
    cursor.execute("delete from student95;")
    for st in combine:
        cursor.execute("""insert into student95 values(%s,%s,%s,%s)""",
                       (int(st[0]),st[1],st[2],int(st[3])))
    conn.commit()
    print("\nData saved into student3 successfully!")


except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()




