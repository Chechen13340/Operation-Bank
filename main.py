from app.utils import get_operations, executed_operations, last_five_operations, sort_time_operation, \
    display_information
from settings import OPEARTION_PATH


operations = get_operations(OPEARTION_PATH)
ex_operations = executed_operations(operations)
five_ex_operations = last_five_operations(ex_operations)
sort_for_date = sort_time_operation(five_ex_operations)
output_information = display_information(sort_for_date)


for number in output_information:
    print(number)