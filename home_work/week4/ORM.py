import sqlite3
class Descriptor(object):
    """Дескриптор данных, который устанавливает и возвращает значения,
       и печатает сообщение о том, что к атрибуту был доступ.
    """

    def __init__(self, initval=None,name=None,base=None,table=None,id_=None):
        self.val = initval
        self.base = base
        self.table = table
        self.id = id_
        self.name = name
        
    
    def __get__(self, obj, objtype):
        
        return self.val
        

    def __set__(self, obj, val):
        
        self.val = val
        
        con = sqlite3.connect(self.base)
        cur = con.cursor()
        
        update = "UPDATE `"+str(self.table)+"` SET `"+str(self.name)+"` = "+str(self.val)+ " WHERE `id` =" + str(self.id)

        cur.execute(update)
        con.commit()
        
        
        cur.close()
        con.close()


class make_class_table:
    def __init__(self,base,table):
        self.base = base
        self.table = table
   
    
    def update_base(self):
        con = sqlite3.connect(self.base)
        cur = con.cursor()
        
        query_columns = "pragma table_info('"+self.table+"')"
        cur.execute(query_columns)
        columns_description = cur.fetchall()
        self.names_columns = [i[1] for i in columns_description]
        
        all_data = "SELECT * FROM `"+self.table+"`"
        cur.execute(all_data)
        self.all_data = cur.fetchall()
        
        
        cur.close()
        con.close()
    
    
    
    def create(self,*args):
        self.update_base()
        self.d = dict(zip(self.names_columns[1:],list(args)))
        columns = ""
        for i in self.d.keys():
            columns += "`"+i+"`,"
           
        
        values = ""
        for i in self.d.values():
            values += "'"+str(i)+"'"+","
        
        insert = "INSERT INTO `"+self.table+"` ("+columns[:-1]+") VALUES "+"("+values[:-1]+")"
        
        con = sqlite3.connect(self.base)
        cur = con.cursor()
        
        cur.execute(insert)
        con.commit()
        
        last_id = "SELECT MAX(id) FROM "+self.table
        cur.execute(last_id)
        last_id = cur.fetchall()
        
        cur.close()
        con.close()
        
        last_id = last_id[0][0]
        
        return self.get(last_id)
        
        
    def get(self,id_):
        self.update_base()
        list_for_find_id = [x[0] for x in self.all_data]
        number_id = list_for_find_id.index(id_)
        
        self.d = dict(zip(self.names_columns,self.all_data[number_id]))
        class_row = type("row", (), {i:Descriptor(self.d[i],i,self.base,self.table,id_) for i in self.d.keys()})
        row = class_row()
        return row
    
    def delete(self,id_):
        self.update_base()
        
        find_list = [i[0] for i in self.all_data]
        
        if id_ not in find_list:
            return f'you have not element whith id={id_}'
        
        delete = "DELETE FROM `"+self.table+"` WHERE `id` ="+str(id_)
        
        con = sqlite3.connect(self.base)
        cur = con.cursor()
        
        cur.execute(delete)
        con.commit()
        
        cur.close()
        con.close()
        
        print('delete success')
        
    def get_all(self):
        self.update_base()
        if len(self.all_data) == 0:
            return'table is empty'
        for i in self.all_data:
            for j in range(len(i)):
                print(f'{self.names_columns[j]} = {i[j]}\n')
            print('---------------------------------------------------\n')
