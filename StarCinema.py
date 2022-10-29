"""
            *** Star Cinema ***
    Small cinema hall management project
    Author: Shajibul Alam Shihab
    Email: shihab77023@gmail.com
    Github: shihab-2021
"""
class Star_Cinema:
    _hall_list = []
    def _entry_hall(self, hall):
        self._hall_list.append(hall)

class Hall(Star_Cinema):
    __seats = {}
    __show_list = []
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols 
        self.__hall_no = hall_no 
        self._entry_hall(vars(self))
    
    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time)) 
        list_of_seats = [[False]*self.__cols for i in range(self.__rows)]
        self.__seats[id] = list_of_seats

    def book_seats(self, name, phone_number, show_id, chose_list):
        print()
        print(f"{'#'*6} TICKET BOOKED SUCCESSFULLY! {'#'*6}")
        print('-'*41)
        print()
        print(f"NAME: {name}")
        print(f"PHONE NUMBER: {phone_number}")
        for show in self.__show_list:
            if show[0]==show_id:
                print(f"MOVIE NAME: {show[1]} \t TIME: {show[2]}")
                break 
        print(f"TICKETS: ", end="")
        for t in chose_list:
            self.__seats[show_id][t[0]][t[1]] = True
            c = chr(t[0]+65)
            print(f"{c}{t[1]}", end=" ")
        print(f"\nHALL: {self.__hall_no}")
        print()
        print('-'*41)
        print()

    def view_shows(self):
        if self.__show_list:
            print()
            print('-'*55)
            print()
            for show in self.__show_list:
                print(f"MOVIE NAME: {show[1]} \t SHOW ID: {show[0]} \t TIME: {show[2]}")
            print()
            print('-'*55)
            print()
        else:
            print("THERE IS NO SHOW FOR TODAY!")

    def view_available_seats(self):
        show_ID = input("ENTER SHOW ID: ")
        flag = 0
        show_info = ()
        for show in self.__show_list:
            if show[0]==show_ID:
                flag = 1
                show_info = show 
                break
        if flag:
            c = 'A'
            print(f"\nMOVIE NAME: {show_info[1]} \t TIME: {show_info[2]}")
            print("X for already booked seats")
            print()
            print('-'*35)
            for row_seats in self.__seats[show_ID]:
                for i, seat in enumerate(row_seats):
                    if seat:
                        print(f"X", end="\t")
                    else:
                        print(f"{c}{i}", end="\t")
                c = chr(ord(c) + 1)
                print()
            print('-'*35)
            print()
        else:
            print(f"\n{'-'*55}\n\nSORRY! THE SHOW ID \"{show_ID}\" YOU HAVE GIVEN IS NOT VALID.\n\n{'-'*55}\n")

    def take_booking_info(self):
        print()
        customer_name = input("ENTER CUSTOMER NAME: ")
        customer_phone_num = input("ENTER CUSTOMER PHONE NUMBER: ")
        while True:
            show_ID = input("ENTER SHOW ID: ")
            flag = 0
            for show in self.__show_list:
                if show[0]==show_ID:
                    flag = 1
                    break
            if flag:
                break
            else:
                print(f"\n{'-'*60}\n\nSORRY! THE SHOW ID \"{show_ID}\" YOU HAVE GIVEN IS NOT VALID.\n\n{'-'*60}\n")
        ticket_num = int(input("ENTER NUMBER OF TICKETS: "))
        ticket_list = []
        for i in range(ticket_num):
            while True:
                seat_no = input("ENTER SEAT NO: ")
                seatNO = seat_no
                if seat_no[0]>='A' and seat_no[0]<='Z':
                    r = ord(seat_no[0])-65
                    seat_no=seat_no.replace(seat_no[0], '')
                    try:
                        c = int(seat_no)
                    except:
                        pass
                    if r<self.__rows and c<self.__cols:
                        if self.__seats[show_ID][r][c]==False:
                            pos = (r, c)
                            flag=1
                            for ticket in ticket_list:
                                if ticket == pos:
                                    flag=0
                                    print(f"\n{'-'*63}\n\nYOU HAVE ALREADY BOOKED THE SEAT \"{seatNO}\"! PLEASE CHOSE ANOTHER ONE.\n\n{'-'*63}\n")
                                    break
                            if flag:
                                ticket_list.append(pos)
                                break
                            else:
                                continue
                        else:
                            print(f"\n{'-'*55}\n\nTHE SEAT \"{seatNO}\" IS ALREADY BOOKED! PLEASE CHOSE ANOTHER ONE.\n\n{'-'*55}\n")
                    else:
                        print(f"\n{'-'*55}\n\nSORRY! SEAT \"{seatNO}\" IS NOT VALID. PLEASE TRY AGAIN.\n\n{'-'*55}\n")
                else:
                    print(f"\n{'-'*55}\n\nSORRY! SEAT \"{seatNO}\" IS NOT VALID. PLEASE TRY AGAIN.\n\n{'-'*55}\n")
        self.book_seats(customer_name, customer_phone_num, show_ID, ticket_list)
			



if __name__ == "__main__":
    hall1 = Hall(4, 5, "SC01")
    hall1.entry_show("S01", "Titanic", "11:20pm")
    hall1.entry_show("S02", "Spider Man", "02:40pm")
    while True:
        print("1. VIEW ALL SHOWS TODAY \n2. VIEW AVAILABLE SEATS \n3. BOOK TICKET \n4. Exit")
        option = input("ENTER OPTION: ")
        if option=='1':
            hall1.view_shows()
        elif option=='2':
            hall1.view_available_seats()
        elif option=='3':
            hall1.take_booking_info()
        else:
            print("\nTHANKS FOR HAVING. IF YOU THINK EXIT IS UNEXPECTED, THEN PLEASE RUN THE PROJECT AGAIN ENTER THE RIGHT OPTION.\n")
            break
