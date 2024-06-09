# test_world.py
import world

def test_world_output(capsys):
    world.print_hello_world()
    captured = capsys.readouterr()
    assert captured.out == "hello world\n"
