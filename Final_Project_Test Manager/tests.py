from functions import *

assert delete_task([], 1) == 0
assert delete_task(['1', '2'], 1) == -1
assert delete_task(['1', '2'], '1') == '2'
assert delete_task(['1', '2'], '-1') == -1
assert delete_task(['1', '2'], '2') == -1

assert is_valid_month([12, 31, 2021]) == False
assert is_valid_day([12, 31, 2021]) == False
assert is_valid_year([12, 31, 2021]) == False
assert is_valid_date('02/29/2020') == True
assert is_valid_date('12/32/2010') == False
assert is_valid_month(["01", "01", "1970"]) == True
assert is_valid_month(["12", "31", "2021"]) == True
assert is_valid_day(["02", "03", "2000"]) == True
assert is_valid_day(["12", "31", "2021"]) == True
assert is_valid_year(["10", "15", "2022"]) == True
assert is_valid_year(["12", "31", "2021"]) == True
assert is_valid_month(["21", "01", "1970"]) == False
assert is_valid_month(["-2", "31", "2021"]) == False
assert is_valid_month(["March", "31", "2021"]) == False
assert is_valid_day(["02", "33", "2000"]) == False
assert is_valid_day(["02", "31", "2021"]) == False
assert is_valid_day(["02", "1st", "2021"]) == False
assert is_valid_day(["14", "1st", "2021"]) == False
assert is_valid_year(["10", "15", "22"]) == False
assert is_valid_year(["12", "31", "-21"]) == False
assert is_valid_date('') == True
assert days_in_feb('2023') == 28
assert days_in_feb('2024') == 29
assert days_in_feb('3000') == 28
assert get_new_task({'name': 'Read', 'info': 'Tolkien', 'rank': '2', 'due': '09/21/2013', 'done': 'eiaou'}) == 'done'
assert get_new_task({'name': 'Read', 'info': 'Tolkien', 'rank': '2', 'due': '09/21/2013', 'done': 'n'}) == {'name': 'Read', 'info': 'Tolkien', 'rank': 2, 'due': '09/21/2013', 'done':False}
assert check_valid_field('name', 'a') == 'name'
assert check_valid_field('name', '') == 'name'
assert check_valid_field('name', 'tada') == 'valid'
assert check_valid_field('rank', '') == 'valid'
assert check_valid_field('rank', '3') == 'valid'
assert check_valid_field('rank', '4') == 'rank'
assert check_valid_field('done', '') == 'done'
assert check_valid_field('done', 'y') == 'valid'
assert check_valid_field('due', '') == 'valid'
assert check_valid_field('due', '10/12/2023') == 'valid'
assert check_valid_field('due', '2/29/2023') == 'due'
assert check_valid_field('money', '2000') == 'money'

assert get_new_task({'name': 'Read', 'info': 'Tolkien', 'rank': '2', 'due': '09/21/2013', 'done': 'eiaou'}) == 'done'
assert get_new_task({'name': 'Read', 'info': 'Tolkien', 'rank': '2', 'due': '09/21/2013', 'done': 'n'}) == {'name': 'Read', 'info': 'Tolkien', 'rank': 2, 'due': '09/21/2013', 'done':False}
assert get_task([], '') == 0
assert get_task([1, 2], '2.3') == -1
assert get_task([1, 2], 2.3) == -1
assert get_task([1, 2], '999') is None
assert get_task([1, 2], 1) == 2
assert update_task({"name": "Collect space dust",
                    "info": "",
                    "rank": 3,
                    "due": "05/28/2042",
                    "done": False}, "name", "") == 'name'
assert update_task({"name": "Collect space dust",
                    "info": "",
                    "rank": 3,
                    "due": "05/28/2042",
                    "done": False}, "due", "12/32/2023") == 'due'
assert update_task({"name": "Collect space dust",
                    "info": "",
                    "rank": 3,
                    "due": "05/28/2042",
                    "done": False}, "due", "12/31/2024") == {"name": "Collect space dust",
                                                                        "info": "",
                                                                        "rank": 3,
                                                                        "due": "12/31/2024",
                                                                        "done": False}
assert update_task({"name": "Collect space dust",
                    "info": "",
                    "rank": 3,
                    "due": "05/28/2042",
                    "done": False}, "done", "y") == {"name": "Collect space dust",
                                                                        "info": "",
                                                                        "rank": 3,
                                                                        "due": "05/28/2042",
                                                                        "done": True}
assert update_task({"name": "Collect space dust",
                    "info": "",
                    "rank": 3,
                    "due": "05/28/2042",
                    "done": False}, "rank", "1") == {"name": "Collect space dust",
                                                                        "info": "",
                                                                        "rank": 1,
                                                                        "due": "05/28/2042",
                                                                        "done": False}
assert update_task({"name": "Collect space dust",
                    "info": "",
                    "rank": 3,
                    "due": "05/28/2042",
                    "done": False}, "rank", "abc") == 'rank'
