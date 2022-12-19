import base
import user_interface as ui

def run():
    employees = base.Database()
    
    while True:
        what_to_do = ui.mode()
        if what_to_do == '1':
            new_employee = ui.what_to_add()
            employees.add(new_employee)
            employees.log()
        if what_to_do == '2':
            info = ui.search()
            to_show = employees.find(info)
            print(to_show)
        if what_to_do == '3':
            id_to_edit = ui.what_to_edit()
            new_data = ui.edit_info()
            employees.edit(id=id_to_edit, data= new_data)
            employees.log()
        if what_to_do == '4':
            id_to_del = ui.what_to_del()
            employees.delete(id=id_to_del)
            employees.log()
        if what_to_do == '5':
            employees.show_all()
        
            
