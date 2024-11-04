# Registration Form

lecture_date = input("Enter date: ").strip()

student_name = input("Enter full name: ").strip().title()

start_time = input("Enter starting time: ").strip()

end_time = input("Enter closing time: ").strip()

signature_pin = int(input("Enter 4 digit pin: ").strip())

attendance = {

    "p1": lecture_date,

    "p2": student_name,

    "p3": start_time,

    "p4": end_time,

    "p5": signature_pin

}


def viewattendance(dictionary):

    print("Attendance")

    for property in dictionary:

        print("___", dictionary[property])


viewattendance(attendance)
input()
