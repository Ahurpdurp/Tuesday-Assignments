import json
import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename


class MenuActions:
    def __init__(self): 
        pass
    def create_initial_tables(self):
        with open("TableStatuses.json") as table:
            all_tables = json.load(table)
            self.all_tables = all_tables
        for x in self.all_tables: #If a table is available, it shouldn't have anything in the time value. 
            if x["Status"] == "Available":
                x["Time"] = None
    def show_status_of_tables(self):
        print("Here are the statuses for all the tables:")
        for x in self.all_tables:
            if not x["Time"]:
                print(f'Table: {x["Table"]}, Status: {x["Status"]}')
            else:
                print(f'Table: {x["Table"]}, Status: {x["Status"]}, Time: {x["Time"]}')
        print("Going back to main menu now.")
    def check_out_table(self):
        for x in range(0,12):
            if self.all_tables[x]["Status"] == "Available":
                break
        else:
            print("No tables are currently available. Going back to main menu.")
            return
        print("Here are all the currently avaiable tables:")
        for x in range(0,12):
            if self.all_tables[x]["Status"] == "Available":
                print(f'Table: {self.all_tables[x]["Table"]}')
        table_number = input("Please enter the table number you want to check out. If you want to return to menu, press 'Q': ")
        while True:
            try:        
                if table_number == 'Q':
                    return                
                while self.all_tables[int(table_number) - 1]["Status"] == "Occupied":
                    table_number = input("This table is occupied. Please choose an available table: ")
                self.all_tables[int(table_number) - 1]
                break
            except:
                table_number = input("Please select one of the available table numbers or press 'Q': ")
        table_number = int(table_number)    
        self.all_tables[table_number - 1]["Status"] = "Occupied"
        now = datetime.datetime.now()
        self.all_tables[table_number - 1]["Time"] = now.strftime("%m/%d/%Y, %H:%M:%S")
        with open("TableStatuses.json", "w") as update_table:
            json.dump(self.all_tables, update_table)
        print(f"Table {table_number} has been checked out. Returning to main menu.")
        return
    def close_table(self):    
        for x in range(0,12):
            if self.all_tables[x]["Status"] == "Occupied":
                break
        else:
            print("No tables to close. Going back to main menu.")
            return
        print("Current tables that are checked out:")
        for x in range(0,12):
            if self.all_tables[x]["Status"] == "Occupied":
                print(f'Table: {self.all_tables[x]["Table"]}, Checked Out Time: {self.all_tables[x]["Time"]}')            
        table_number = input("What table do you want to close? If you want to return to the menu, press 'Q': ")
        while True:
            try:        
                if table_number == 'Q':
                    return                
                while self.all_tables[int(table_number) - 1]["Status"] == "Available":
                    table_number = input("This table is available. Please choose an occupied table: ")
                self.all_tables[int(table_number) - 1]
                break
            except:
                table_number = input("Please select one of the available table numbers or press 'Q': ")
        table_number = int(table_number)      
        self.all_tables[table_number - 1]["Status"] = "Available"
        now = datetime.datetime.now()
        current_time = now.strftime("%H %M")
        current_time_value = int(current_time[0:2]) * 60 + int(current_time[3:5])
        checked_time_value = 60 * int(self.all_tables[table_number - 1]["Time"][12:14]) + int(self.all_tables[table_number - 1]["Time"][15:17])
        total_time = current_time_value - checked_time_value
        total_cost = total_time * 30 / 60
        if total_time < 0:
            total_time += 24*60 #in case the pool place opens through midnight ex. 00:30 - 11:30 from the day before
        print(f"Total time played was {total_time//60} hours and {total_time%60} minutes. The total is ${total_cost}")
        with open("TableStatuses.json", "w") as update_table:
            json.dump(self.all_tables, update_table)
        x = self.all_tables[table_number - 1]    
        txt_log = f"Table: {table_number} Start Time: {self.all_tables[table_number-1]['Time']} \
End Time: {now.strftime('%m/%d/%Y, %H:%M:%S')} Total Time Played: {total_time} minute(s) Cost: ${total_cost}"
        file_name = f'{now.strftime("%m-%d-%Y")} Log.txt'
        self.file_name = file_name
        with open(file_name, "a+") as update_log:
            update_log.write(txt_log)
            update_log.write('\n')
        self.all_tables[table_number - 1]["Time"] = None #reset the time for the next customer
    def email_report(self):
        now = datetime.datetime.now()
        if not os.path.isfile(f'{now.strftime("%m-%d-%Y")} Log.txt'):
            print("Daily log not yet created. No sales today so far. Going back to main menu.")
            return
        send_to = input("Please enter your full email address. To go back to main menu, press 'Q': ")
        while "@" not in send_to or "." not in send_to:
            if send_to == "Q":
                return
            send_to = input("Please enter the full email address or press 'Q' (ex. JohnDoe@gmail.com) ")    
        send_from = "pool.software.digitalcrafts@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to  
        msg['Subject'] = f'{now.strftime("%m-%d-%Y")} Log'
        msg.attach(MIMEText(f"Hi, \n \nHere are all the sales for {now.strftime('%m-%d-%Y')}. Please do not reply to this email. Thank you."))
        files = f'{now.strftime("%m-%d-%Y")} Log.txt'
    
        with open(f'{now.strftime("%m-%d-%Y")} Log.txt', "rb") as fil: 
            attachedfile = MIMEApplication(fil.read())
            attachedfile.add_header(
                'content-disposition', 'attachment', filename=basename(files) )
            msg.attach(attachedfile)

        smtp = smtplib.SMTP(host="smtp.gmail.com", port= 587) 
        smtp.starttls()
        smtp.login("pool.software.digitalcrafts@gmail.com","testdigitalcrafts")
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()
        print(f"Email has been sent to {send_to}. Going back to main menu now.")
        return

menu_action = MenuActions()
menu_action.create_initial_tables()
input_answer = ""
while input_answer != "5":
    input_answer = input("Please select one of the actions on the menu: \n 1) See all tables.  \n \
2) Check out a table. \n 3) Close a table. \n 4) Email Daily Report \n 5) Quit the menu \n Your selection: ")
    if input_answer == "1":
        menu_action.show_status_of_tables()
    if input_answer == "2":
        menu_action.check_out_table()
    if input_answer == "3":
        menu_action.close_table()
    if input_answer == "4":
        menu_action.email_report()
print("See you next time!")