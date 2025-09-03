class DataProgram:
    def __init__(self):
        self.storage_balance = 1000.00  # Solde initial

    def process_operation(self, passed_operation, balance=None):
        operation_type = passed_operation.strip().upper()

        if operation_type == "READ":
            return self.storage_balance
        elif operation_type == "WRITE":
            if balance is not None:
                self.storage_balance = balance
        else:
            print("Unknown operation type.")