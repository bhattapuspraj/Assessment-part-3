from task2 import  ferry_service_total()
def booking_approval():
    status = "Pending"
    print(f"Status: {status}")
    
    if status == "Approved":
        approval_ref= ID_Number[3:] + Ticket_id[-2:]

        print(f"Approval Ref: {approval_ref}")
    else:
        print("still pending approvel.")


ID_Number, Passenger_Name = customer_booking()
total_cost, items_price = ferry_service_total

print("Enter the information of booking approvel:")
print(f"Passenger Name: {Passenger_Name}")
print(f"ID Number: {ID_Number}")
print(f"Total Cost: ${total_cost:.2f}")

booking_approval()






