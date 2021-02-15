from input_parser import InputParser

def test_given_age_as_string_when_running_ager_returns_argument_error():
    import subprocess
    output = subprocess.run('python ager.py -name jasvir -age fgt', stdout=subprocess.PIPE)
    assert output.stdout.decode('utf-8').strip() == "Argument Error"

def test_given_age_as_number_when_running_ager_no_error():
    import subprocess
    output = subprocess.run('python ager.py -name jasvir -age 21', stdout=subprocess.PIPE)
    assert output.stdout.decode('utf-8').strip() != "Argument Error"



