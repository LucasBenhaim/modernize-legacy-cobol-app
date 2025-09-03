class Operations:
    def __init__(self, data_program):
        self.data_program = data_program

    def process(self, passed_operation):
        operation_type = passed_operation.strip().upper()

        if operation_type == "TOTAL":
            final_balance = self.data_program.process_operation("READ")
            print(f"\nCurrent balance: {final_balance:.2f}\n")

        elif operation_type == "CREDIT":
            try:
                amount = float(input("Enter credit amount: "))
            except ValueError:
                print("Invalid amount entered.")
                return

            final_balance = self.data_program.process_operation("READ")
            final_balance += amount
            self.data_program.process_operation("WRITE", final_balance)
            print(f"Amount credited. New balance: {final_balance:.2f}\n")

        elif operation_type == "DEBIT":
            try:
                amount = float(input("Enter debit amount: "))
            except ValueError:
                print("Invalid amount entered.")
                return

            final_balance = self.data_program.process_operation("READ")
            if final_balance >= amount:
                final_balance -= amount
                self.data_program.process_operation("WRITE", final_balance)
                print(f"Amount debited. New balance: {final_balance:.2f}\n")
            else:
                print("Insufficient funds for this debit.\n")

        else:
            print("Unknown operation type.\n")