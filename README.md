# Assessment-part-3
**About Repository.**
All programming work along with research gets stored within this repository. The repository holds programming code that I authored as well as practice-oriented and learned programming code. Programmer fundamental explanations together with their applications within real-world implementation examples are also added. The main purpose of this repository serves to learn optimal coding techniques for future application while working on new code or reviewing existing code.

The repository features clear folder organization for files and includes code explanations through comments that describe program activities. My storage space functions to house program code while simultaneously providing a space to evaluate knowledge retention and enhance my programming technique.

**What does my code do ?**
The task333.py represents a fundamental ferry booking system developed in Python programming language. It performs the following tasks:
The script contains customer_booking() as a tool to get name and ID along with ticket number from passengers.
The code executes price calculation through the second function ferry_service_total().
The program displays booking data which includes total cost and passenger identities together with names.
The last step calls booking_approval() to determine the booking status between approved and pending.
Code management becomes easier through functions that divide operations in a streamlined manner.

**Programming Principles Used.**
**Modularity:**
Due to the individual function-based approach each task functions operates independently which enhances code testing and modification the processes. eg:customer_booking and ferry_service_total

**speration of concerns:**
The program divides its operations into distinct parts to create code that is simplified for understanding. eg: booking_approval() checks only the status.

**Maintainability:**
Updating a single part in the document will suffice instead of modifying the entire file. eg: code is organized in function.

**Readability:**
The added comments provide understanding to myself and there other developers for the code operation. eg:code has commented.

**Things that can be improved.**
Although the code functions correctly some changes could enhance its effectiveness:

The system preloads the booking status value with "Pending". The system needs customization either through user selection or automatic process determination according to the circumstances.

The program uses two variables ID_Number and Ticket_id in a global context. A more effective solution would be to transport these variables through arguments in functions because it creates cleaner code with enhanced protection.

Somewhere in the program the word "approvel" contains an incorrect spelling which should read "approval". Small corrections in program code improvement enhances both the professionalism and readability of the program code.
