import base
import user_interface as ui

def run():
    contacts = base.Database()
    
    while True:
        what_to_do = ui.mode()
        if what_to_do == '1':
            new_contact = ui.what_to_add()
            contacts.add(new_contact)
            contacts.log()
        if what_to_do == '2':
            info = ui.search()
            to_show = contacts.find(info)
            ui.show(to_show)
        if what_to_do == '3':
            contacts.show_all()
        
            
