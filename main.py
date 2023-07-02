from settings import OPEARTION_PATH
from utils import get_operations, executed_operations, sort_time_operation, last_five_operations, display_information

operations = get_operations(OPEARTION_PATH)
ex_operations = executed_operations()
five_ex_operations = last_five_operations()
sort_for_date = sort_time_operation()
output_information = display_information()


for number in output_information:
    print(number)