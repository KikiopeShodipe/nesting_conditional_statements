medical_cause = input("Do you have a medical cause? (Y/N): ")
attendance = float(input("Enter you attendance percentage: "))
if medical_cause == 'Y':
    print("Allowed to take the exam due to medical cause.")
elif medical_cause == 'N':
    if attendance > 75:
        print("Allowed to take the exam based on attendance.")
    else:
        print("Not allowed to take the exam due to low attendance.")
else:
    print("Invalid input for medical cause. Use 'Y' or 'N'.")